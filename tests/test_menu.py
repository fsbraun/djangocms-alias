from cms.toolbar.utils import get_object_edit_url

from djangocms_alias.utils import is_versioning_enabled

from .base import BaseAliasPluginTestCase


class AliasMenuTestCase(BaseAliasPluginTestCase):
    def test_alias_pages_have_no_menu_nodes(self):
        alias = self._create_alias()
        with self.login_user_context(self.superuser):
            response = self.client.get(get_object_edit_url(alias.get_content()))
            if is_versioning_enabled() and False:
                self.assertNotContains(response, '<ul class="nav">')
            else:
                self.assertInHTML('<ul class="nav"></ul>', response.content.decode())

    def test_pages_keep_their_menu_nodes(self):
        """Tests that AliasDisableMenu modifier does not affect
        non-alias pages"""

        response = self.client.get(self.page.get_absolute_url())

        self.assertInHTML(
            '<ul class="nav"><li class="child selected"><a href="/en/test/">test</a></li></ul>',  # noqa: E501
            response.content.decode(),
        )
