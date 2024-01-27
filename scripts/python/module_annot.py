import json
import re
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd


def get_modules(pom_path):
    """Uses regex to find the names of the modules. Modules are in between <module> and </module> tags."""
    module_re = re.compile(r"<module>(.*?)</module>", re.DOTALL)
    with open(pom_path, 'r') as pom_file:
        pom = pom_file.read()
    modules = module_re.findall(pom)

    return modules


def best_annotation(annotations, taxonomy):
    module_annot = np.mean(annotations, axis=0)
    #sorted_labels = np.argsort(module_annot)[::-1]
    return module_annot, [taxonomy[x] for x in range(len(module_annot))]


def run():
    dataset_path = Path("/home/sasce/PycharmProjects/AutoFL/data/raw/zaki_data.csv")
    annotation_path = Path("/home/sasce/PycharmProjects/AutoFL/data/out")
    repo_path = Path("/home/sasce/PycharmProjects/AutoFL/data/raw/repository")
    projects = pd.read_csv(dataset_path)['name']
    entries = []
    for project in projects:
        modules_annotation = defaultdict(lambda: list())
        project_annot = json.load(open(annotation_path.joinpath(f"{project}.json"), 'r'))
        annotation = project_annot["versions"][0]
        try:
            pom_path = repo_path.joinpath(project).joinpath("pom.xml")
            modules_names = get_modules(pom_path)
        except:
            modules_names = []
        taxonomy = {int(k): v for k, v in project_annot['taxonomy'].items()}

        skipped_files = 0
        for file_name in annotation['files']:
            file_module = file_name.split('/')[0]
            if file_module not in modules_names:
                skipped_files += 1

            if not annotation['files'][file_name]['annotation']['unannotated']:
                modules_annotation[file_module].append(annotation['files'][file_name]['annotation']['distribution'])
        print(f"{project} - Skipped {skipped_files} files")


        print(modules_annotation.keys())
        for module in modules_annotation:
            res = {"project": project}
            annot, labels = best_annotation(modules_annotation[module], taxonomy)
            res["module"] = module
            res['labels'] = labels
            res['distribution'] = list(annot)
            entries.append(res)

    out_path = Path("/home/sasce/PycharmProjects/AutoFL/data/module_annotation.csv")
    df = pd.DataFrame(entries)
    df.to_csv(out_path, index=False)


if __name__ == '__main__':
    run()
