from countershape.doc import *

pages = [
            Page(
                "markdown/markdown.md",
                title="Markdown",
                pageTitle = "Mark Up with MarkDown"
            ),
            Directory("markdown"),
            
            Page(
                "rest/rest.rst",
                title="reStructuredText",
                pageTitle = "reStructuredText"
            ),           
            Directory("rest"),
            
            Page(
                "textish/textish.html",
                title="Textish",
                pageTitle = "Mark Up with MarkDown"
            ),
            Directory("textish"),
        ]
        
