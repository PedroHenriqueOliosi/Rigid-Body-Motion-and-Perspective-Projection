from Config import *
import Camera
from stl import mesh

class Object(Camera):
    def __init__(self):
        super.__init__()

        self.file = 'smurfcat.stl'

    def STL(self):
        self.your_mesh = mesh.Mesh.from_file(self.file)
        self.x = self.your_mesh.x.flatten()
        self.y = self.your_mesh.y.flatten()
        self.z = self.your_mesh.z.flatten()

        self.vectors = self.your_mesh.vectors

        self.indo_ali = np.array([self.x.T,self.y.T,self.z.T,np.ones(self.x.size)])

    def image_projection_matrix(self):
        self.M = self.K@BASE_CANON@self.g@self.indo_ali
        return self.M