from collections import defaultdict
from typing import Tuple

import numpy as np

from entity.project import Project, Version
from pipeline.pipeline import PipelineBase


class PackageAnnotationPipeline(PipelineBase):
    def __init__(self):
        pass

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        packages_annot = defaultdict(list)
        for file_name in version.files:
            file = version.files[file_name]
            if file.annotation.unannotated:
                continue
            packages_annot[file.package].append(file.annotation.distribution)

        for package in packages_annot:
            annot = np.mean(packages_annot[package], axis=0)
            version.package_annotation[package] = list(annot)

        return project, version
