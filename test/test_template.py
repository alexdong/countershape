import countershape
import libpry
from testpages import *


class uSyntax(countershape.test.DummyState):
    def test_simple_syntax(self):
        assert countershape.template.pySyntax("def foo")

    def test_syntax_withConf(self):
        p = countershape.template.pySyntax.withConf(
                style="emacs",
                linenos="inline",
                linenostep=5,
                cssClass="bar"
            )
        assert p("def foo")


class uNS(countershape.test.DummyState):
    def setUp(self):
        self.d = countershape.doc._DocRoot("doctree")
        self.application = countershape.doc._DocApplication(self.d)
        self.pageName = "/test.html"
        countershape.test.DummyState.setUp(self)

    def test_syntax_next(self):
        p = countershape.template._ns()["next"]
        assert p.title == "Test"

    def test_syntax_previous(self):
        p = countershape.template._ns()["previous"]
        assert not p


class ucubescript(libpry.AutoTree):
    def test_simple(self):
        t = """
            @_!asdf!@
            $_!asdf!$
            <!--(_for foo in bar)-->
            <!--(_block bar)-->
        """
        out = countershape.template.cubescript(t)
        assert "@!asdf!@" in out
        assert "$!asdf!$" in out
        assert "<!--(for foo in bar)-->" in out
        assert "<!--(block bar)-->" in out


class uTemplate(countershape.test.DummyState):
    def test_str(self):
        s = """
            top@!top!@top
            linkTo@!linkTo("TestPage")!@linkTo
            urlTo@!urlTo("TestPage")!@urlTo
            name@!this.name!@name
        """
        t = countershape.template.Template(False, s, this=countershape.state.page)
        s = str(t)
        assert "top.top" in s
        assert "linkTo<a href" in s
        assert "urlToTestPage" in s
        assert "nameTestPage" in s

    def test_textish(self):
        s = """
            _this is bold_
        """
        t = countershape.template.Template(True, s)
        assert "<em>" in str(t)


class uFileTemplate(countershape.test.DummyState):
    def setUp(self):
        self.application = TestApplication(
            countershape.BaseRoot(
                [
                    TPageHTMLFileTemplate(),
                ]
            )
        )
        self.pageName = "TPageHTMLFileTemplate"
        countershape.test.DummyState.setUp(self)

    def test_foo(self):
        s = self.call("TPageHTMLFileTemplate")
        assert "nameTPageHTMLFileTemplatename" in s


tests = [
    uSyntax(),
    uNS(),
    ucubescript(),
    uTemplate(),
    uFileTemplate()
]
