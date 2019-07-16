# A script to replace a prefix from selected objects. E.g. 'pasted__'.

import maya.cmds as cmds

height = 100
width = 200

class mayaprefixreplacer:
    def __init__(self):
        self.window = 'prefixreplacer'
        self.title = "Prefix Replacer"
        self.size = (height, width)

    def buildUI(self):
        if cmds.window(self.window, exists=True) == True:
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        #self.mainForm = cmds.formLayout(numberOfDivisions=100)
        cmds.rowColumnLayout(width=width)
        cmds.text(label="Prefix Replacer", font="boldLabelFont")
        cmds.text(label="A script to replace a prefix of any \n object within the scene.")
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, width/2), (2, width/2)])
        cmds.text(label="Prefix")
        self.prefix = cmds.textField("prefix")
        cmds.text(label="Replace With")
        self.replace = cmds.textField("replace")
        cmds.rowColumnLayout(numberOfColumns=1, width=width)
        cmds.button("Remove", command=self.removeBtn)
        cmds.rowColumnLayout(width=width)
        cmds.showWindow()

    def removeBtn(self, *args):
        prefix=cmds.textField(self.prefix, query=True, text=1)
        replace=cmds.textField(self.replace, query=True, text=1)
        selection=cmds.ls((prefix+"*"), selection=True)
        for object in selection:
            newname=object.replace(prefix, replace)
            cmds.rename(object, newname)

prefixreplacer = mayaprefixreplacer()
prefixreplacer.buildUI()
