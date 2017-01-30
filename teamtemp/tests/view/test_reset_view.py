from django.core.urlresolvers import reverse

from teamtemp.tests.view.admin_only_view_testcase import AdminOnlyViewTestCase


class AdminViewTestCases(AdminOnlyViewTestCase):
    def test_no_admin_reset_view(self):
        response = self.client.get(reverse('reset', kwargs={'survey_id': self.teamtemp.id}), follow=True)
        self.assertIsPasswordForm(response)

    def test_admin_reset_team_view(self):
        self.setUpAdmin()
        response = self.client.get(reverse('reset', kwargs={'survey_id': self.teamtemp.id}), follow=True)
        self.assertIsNotPasswordForm(response)
        self.assertIsAdminForm(response)