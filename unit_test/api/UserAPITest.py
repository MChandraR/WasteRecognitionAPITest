from api.APITest import APITest

class UserAPITest(APITest):
    def test(self):
        print("\n\n=================================[API User Testing]=========================================\n\n")
        self.get_user_count_api_test()
        self.get_user_info()
        self.testUserRegister()
        print("\n\n=================================[END User Testing]=========================================\n\n")


    def get_user_count_api_test(self):
        response = self.request("GET", "users/count").json()
        if response["status"] == 200  and response["data"]["total_users"] and type(response["data"]["total_users"]) is int:
            print("✅ [User Test] User count valid")
            return
        raise Exception
    
    def get_user_info(self):
        response = self.request("GET", "users").json()
        admin_response = self.admin_request("GET", "users").json()

        if admin_response["status"] == 200  and admin_response["data"] is not None:
            print("✅ [Admin Test] User count valid")
            if response["status"] == 403  and response["data"] is None:
                print("✅ [User Test] User count valid")
                return
            else :
                print("❌ [User Test] User Request harus forbidden ")
        raise Exception
    
    def get_user_info(self):
        response = self.request("GET", "users").json()
        admin_response = self.admin_request("GET", "users").json()

        if admin_response["status"] == 200  and admin_response["data"] is not None:
            print("✅ [Admin Test] User count valid")
            if response["status"] == 403  and response["data"] is None:
                print("✅ [User Test] User count valid")
                return
            else :
                print("❌ [User Test] User Request harus forbidden ")
        raise Exception
    
    def testUserLogin(self, payload = None):
        if payload is None:
            payload = {
                "username" : "tester_1",
                "password" : "tester"
            }
        response = self.request("POST", "auth/login", payload= payload).json()

        if response["status"] == 200 :
            print("✅ [User Test] Check user permission on login")
            return
        else:
            print("❌ [User Test] Server should block user request on login ")
        raise Exception
    
    def testUserRegister(self):
        payload = {
            "username" : "tester_1",
            "password" : "tester",
            "email" : "testeraccount@gmai.com",
            "role" : "user",
            "is_assigned" : True
        }
        payload2 = {
            "username" : "tester_2",
            "password" : "tester",
            "email" : "testeraccount@gmai.com",
            "role" : "user",
            "is_assigned" : True
        }
        response = self.request("POST", "auth/register", payload= payload).json()

        if response["status"] == 403 :
            print("✅ [User Test] Check user permission on registering new account")
            response_admin = self.admin_request("POST", "auth/register", payload= payload2).json()
            if response_admin["status"] == 201 : 
                print("✅ [Admin Test] Pembuatan akun dari admin berhasil")
                self.testUserLogin(payload=payload2)
                self.checkUpdateUser(response_admin["data"]["id"])
                return
            else:
                print("❌ [Admin Test] Gagal mendaftarakan akun baru ")
        else:
            print("❌ [User Test] Server should block user request on registering new account ")
        raise Exception
    
    def checkUpdateUser(self, user_id : str):
        payload = {
            "id" : user_id,
            "username" : "tester_1_new",
            "password" : "tester",
            "email" : "testeraccount@gmai.com",
            "role" : "user",
            "is_assigned" : True
        }

        response = self.request("PUT", "users", payload=payload).json()
        if response["status"] == 403:
            admin_response = self.admin_request("PUT", "users", payload=payload).json()
            print("✅ [User Test] User update prevention valid")
            if admin_response["status"] == 200 :
                print("✅ [User Test] User update prevention valid")

                user_data = self.getUserById(user_id=user_id)
                if user_data["username"] == payload["username"] and user_data["email"] == payload["email"]:
                    self.deleteUserById(user_id=user_id)
                    return 
                print("❌ [admin Test] Data akun tidak terupdate di database ! ")

            else:             
                print("❌ [Admin Test] Gagal melakukan update data akun oleh admin ")
        else:
            print("❌ [User Test] Gagal mencegah manipulasi data akun oleh user ")


        raise Exception
    

    def getUserById(self, user_id : str):
        response = self.request("GET", f"users/{user_id}").json()
        admin_response = self.admin_request("GET", f"users/{user_id}").json()

        if response["status"] == 403:
            print("✅ [User Test] Berhasil mencegah user menadpatkan data user lain !")
            if admin_response["status"] == 200 and admin_response["data"] is not None:
                print("✅ [Admin Test] User count valid")
                return admin_response["data"]
        else:
            print("❌ [User Test] IDOR data user")

        raise Exception
    
    def deleteUserById(self, user_id : str):
        response = self.request("DELETE", f"users?id={user_id}").json()

        if response["status"] == 403:
            admin_response = self.admin_request("DELETE", f"users?id={user_id}").json()
            print("✅ [User Test] Berhasil mencegah user menghapus data user lain !")
            if admin_response["status"] == 200 :
                print("✅ [Admin Test] Admin berhasil menghapus data user")
                return admin_response["data"]
        else:
            print("❌ [User Test] IDOR data user")

        raise Exception
 
