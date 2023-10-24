from typing import Tuple, List, Union, Any, Dict

from omegaconf import OmegaConf
from tqdm import tqdm

from annotation.annotator import Annotator
from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation
from entity.project import Project, Version
from pipeline.pipeline import PipelineBase


class FileAnnotationPipeline(PipelineBase):
    def __init__(self,
                 annotators: List[Annotator],
                 ensemble: Union[EnsembleBase, callable],
                 taxonomy,
                 cfg=None):

        self.annotators = annotators
        self.ensemble = ensemble
        self.taxonomy = taxonomy
        self.cfg = cfg if cfg else {}

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        project.cfg = self.cfg
        project.taxonomy = {str(index): self.taxonomy.id_to_label[index].name for index in self.taxonomy.id_to_label}
        for file_name in tqdm(version.files, desc=f"Labelling files for {project.name} @ version: {version.commit_id}"):
            file = version.files[file_name]
            file_label_vecs = []
            lfs_unannotated = []
            for annotator in self.annotators:
                label_vec, unannotated = annotator.annotate(file.path, " ".join(file.identifiers))
                lfs_unannotated.append(unannotated)
                file_label_vecs.append(label_vec)

            unannotated = bool(all(lfs_unannotated))
            label_vec = self.ensemble(file_label_vecs)
            file.annotation = Annotation(distribution=list(label_vec), unannotated=unannotated)

        return project, version
