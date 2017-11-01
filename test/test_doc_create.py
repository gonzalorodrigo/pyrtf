from PyRTF import Document, Section, Renderer
import unittest


class TestDocCrate(unittest.TestCase):
    
    def test_write_doc(self):
        filename="file.rtf"
        doc = Document()
        section = Section()
        doc.Sections.append(section)
        section.append("SOME TEXT")
        section.append("more TEXT")
        section.append("")
        
        section = Section()
        doc.Sections.append(section)
        section.append("SOME TEXT2")
        
        with open(filename, "w") as f:
            DR = Renderer()
            DR.Write(doc, f)