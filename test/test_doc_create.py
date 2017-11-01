from PyRTF import Document, Section, Renderer
import os
import unittest


class TestDocCrate(unittest.TestCase):
    
    def test_write_doc(self):
        
        self.addCleanup(os.remove, "file.rtf")
        self.assertFalse(os.path.isfile("file.rtf"),
                         "File Exists before test.")
        doc = Document()
        section = Section()
        doc.Sections.append(section)
        section.append("SOME TEXT")
        section.append("more TEXT")
        section.append("")
        
        section = Section()
        doc.Sections.append(section)
        section.append("SOME TEXT2")
        
        with open("file.rtf", "w") as f:
            DR = Renderer()
            DR.Write(doc, f)
        
        self.assertTrue(os.path.isfile("file.rtf"))
        