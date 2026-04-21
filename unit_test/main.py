from api.UserAPITest import UserAPITest
from api.GlobalModelAPITest import GlobalModelAPITest

unit_test   = [
    UserAPITest(),
    GlobalModelAPITest()
]

for ut in unit_test:
    ut.test()