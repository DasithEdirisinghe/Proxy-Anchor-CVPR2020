import os
import torchvision.datasets as datasets
from .base import BaseDataset

class Rabot(BaseDataset):
    def __init__(self, root, mode, transform=None):
        self.root = root + '/new_custom_dataset_expanded'
        self.mode = mode
        self.transform = transform

        # The total number of classes in the dataset
        num_classes = 22

        if self.mode == 'train':
            self.classes = range(0, 11)
        elif self.mode == 'eval':
            self.classes = range(11, num_classes)

        BaseDataset.__init__(self, self.root, self.mode, self.transform)
        # Use torchvision.datasets.ImageFolder to load the dataset from the folder structure
        image_folder = datasets.ImageFolder(root=self.root, transform=self.transform)

        # Filter images based on the specified classes and mode
        self.ys = []
        self.I = []
        self.im_paths = []
        for index, (image_path, label) in enumerate(image_folder.imgs):
            if label in self.classes:
                # fn needed for removing non-images starting with `._`
                fn = os.path.split(image_path)[1]
                if not fn.startswith('._'):  # Exclude files starting with '._'
                    self.ys.append(label)
                    self.I.append(index)
                    self.im_paths.append(image_path)
