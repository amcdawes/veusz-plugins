from veusz.plugins import *
from numpy import genfromtxt, shape

class ImportPluginExample(ImportPlugin):
    """An example plugin for reading a set of unformatted numbers
    from a file."""

    name = "Tektronix CSV plugin"
    author = "Andrew M. C. Dawes"
    description = "Import data columns from a Tektronix scope CSV file"

    # Uncomment this line for the plugin to get its own tab
    promote_tab = 'Tektronix'

    #file_extensions = set(['.example'])

    def __init__(self):
        ImportPlugin.__init__(self)
        self.fields = []

    def doImport(self, params):
        """Actually import data
        params is a ImportPluginParams object.
        Return a list of ImportDataset1D, ImportDataset2D objects
        """

        f = params.openFileWithEncoding()
        data = genfromtxt(f, delimiter=",")
        available_channels=shape(data)[1]/6 # assumes 6 cols per channel
        DataList = []
        name_list = [["ch1x","ch1y"],["ch2x","ch2y"],["ch3x","ch3y"],["ch4x","ch4y"]]
        for i in range(available_channels):
            col = 3 + i*6
            DataList.append(ImportDataset1D(name_list[i][0], data[:,col]))
            DataList.append(ImportDataset1D(name_list[i][1], data[:,col+1]))

        return DataList

importpluginregistry.append(ImportPluginExample())

