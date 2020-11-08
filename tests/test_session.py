from odoo.tests import common

class TestSession(common.TransactionCase):
    def setUp(self):
        super(TestSession, self).setUp()
        self.session = self.env['openacademy.session']
        self.session1 = self.session.create({'name': 'Aerospace session', 'start_date': '11/10/2020',
                                              'duration': '60.00', 'seats': '10', 'instructor_id': 'Alice',
                                              'course_id': 'Aerospace', 'attendee_ids': 'Tiya'})
        self.session2 = self.session.create({'name': 'Aviation session', 'start_date': '12/10/2020',
                                              'duration': '120.00', 'seats': '10', 'instructor_id': 'Sunny',
                                              'course_id': 'Aerospace', 'attendee_ids': 'Miya'})

        def test_compute_taken_seats(self):
            self.assertEqual(self.session.taken_seats, 1)
            self.assertEqual(self.session.taken_seats, 1)
            self.session2.write({'attendee_ids':'Liya'})
            self.assertEqual(self.session2.taken_seats, '2')