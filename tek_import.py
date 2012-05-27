from veusz.plugins import *
from numpy import genfromtxt

class ImportPluginExample(ImportPlugin):
    """An example plugin for reading a set of unformatted numbers
    from a file."""

    name = "Tektronix CSV plugin"
    author = "Andrew M. C. Dawes"
    description = "Import data columns from a Tektronix scope CSV file"

    # Uncomment this line for the plugin to get its own tab
    promote='Tektronix'

    file_extensions = set(['.example'])

    def __init__(self):
        ImportPlugin.__init__(self)
        self.fields = [
            ImportFieldCombo("channels", descr="Number of channels to import", items=("1", "2", "3", "4"),
                             editable=False, default="1")
            ]

    def doImport(self, params):
        """Actually import data
        params is a ImportPluginParams object.
        Return a list of ImportDataset1D, ImportDataset2D objects
        """

        f = params.openFileWithEncoding()
        data = genfromtxt(f, delimiter=",")
        chans = int(params.field_results["channels"])
        column_indeces = [3,4]
        return [ImportDataset1D("ch1x", data[:,3]),
                ImportDataset1D("ch1y", data[:,4])]


importpluginregistry.append(ImportPluginExample())

