from api.APITest import APITest
import json

class GlobalModelAPITest(APITest):
    def test(self):
        print("\n\n=============================[API Global Model Testing]=====================================\n\n")
        self.get_global_model_info()
        self.test_global_model_evaluate_for_user()
        #self.test_global_model_evaluate_for_admin()
        self.test_get_all_weight_data_for_admin()
        self.test_get_all_weight_data_for_user()
        #self.test_download_model_weights()
        self.test_get_classifier_parameters()
        self.test_save_classifier_parameters_for_user()
        self.test_save_classifier_parameters_for_admin()    
        # self.test_model_update_for_user()
        # self.test_model_update_for_admin()
        self.test_add_model_weight()
        print("\n\n=============================[END Global Model Testing]=====================================\n\n")

    def get_global_model_info(self):
        response = self.request("GET", "model/info").json()

        if response["status"] == 200  and response["data"] is not None:
            print("✅ [Global Model Test] Mendapatkan informasi global model berhasil")
            return
        else :
            print("❌ [Global Model Test] Gagal mendapatkan informasi global model ")
        raise Exception
    
    def test_global_model_evaluate_for_user(self):
        response = self.request("GET", "model/evaluate").json()

        if response["status"] == 403  and response["data"] is None:
            print("✅ [Global Model Test] Berhasil mencegah user melakukan evaluasi global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user melakukan evaluasi global model ")
        raise Exception
    
    def test_global_model_evaluate_for_admin(self):
        response = self.admin_request("GET", "model/evaluate").json()
        if response["status"] == 200 :
            print("✅ [Global Model Test] Berhasil mendapatkan evaluasi global model ")
            return
        else :
            print("❌ [Global Model Test] Admin tidak bias melakukan evaluasi global model ")
        raise Exception
    
    def test_get_all_weight_data_for_admin(self):
        response = self.admin_request("GET", "model/weights").json()
        if response["status"] == 200 and response["data"] is not None:
            print("✅ [Global Model Test] Berhasil mendapatkan semua data bobot global model ")
            return
        else :  
            print("❌ [Global Model Test] Gagal mendapatkan semua data bobot global model ")
        raise Exception
    
    def test_get_all_weight_data_for_user(self):
        response = self.request("GET", "model/weights").json()
        if response["status"] == 403 and response["data"] is None:
            print("✅ [Global Model Test] Berhasil mencegah user mendapatkan semua data bobot global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user mendapatkan semua data bobot global model ")
        raise Exception
    
    def test_download_model_weights(self):
        response = self.request("GET", "model/download")
        if response.status_code == 200 :
            print("✅ [Global Model Test] Berhasil mendownload bobot global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal mendownload bobot global model ")
        raise Exception
    
    def test_get_classifier_parameters(self):
        response = self.request("GET", "model/classifier/weight").json()
        if response["status"] == 200 and response["data"] is not None:
            print("✅ [Global Model Test] Berhasil mendapatkan parameter classifier global model ")
            return
        else :  
            print("❌ [Global Model Test] Gagal mendapatkan parameter classifier global model ")
        raise Exception
    
    def test_get_classifier_parameters(self):
        response = self.request("GET", "model/classifier/weight").json()
        if response["status"] == 200 and response["data"] is not None:
            print("✅ [Global Model Test] Berhasil mendapatkan parameter classifier global model ")
            return
        else :  
            print("❌ [Global Model Test] Gagal mendapatkan parameter classifier global model ")
        raise Exception
    
    def test_save_classifier_parameters_for_user(self):
        response = self.request("GET", "model/classifier/save_param")
        if response.status_code == 403 :
            print("✅ [Global Model Test] Berhasil mencegah user menyimpan parameter classifier ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user menyimpan parameter classifier ")
        raise Exception
    
    def test_save_classifier_parameters_for_admin(self):
        response = self.admin_request("GET", "model/classifier/save_param")
        if response.status_code == 200 :
            data = response.json()
            print("✅ [Global Model Test] Berhasil menyimpan parameter classifier ")
            self.test_delete_classifier_weights_for_user(data["data"]["id"])
            self.test_delete_classifier_weights_for_admin(data["data"]["id"])
            return
        else :
            print("❌ [Global Model Test] Gagal menyimpan parameter classifier ")
        raise Exception
    
    def test_delete_classifier_weights_for_user(self, user_id : str):
        response = self.request("DELETE", f"model/classifier/weight/{user_id}")
        if response.status_code == 403 :
            print("✅ [Global Model Test] Berhasil mencegah user menghapus parameter classifier global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user menghapus parameter classifier global model ")
        raise Exception
    
    def test_delete_classifier_weights_for_admin(self, user_id : str):
        response = self.admin_request("DELETE", f"model/classifier/weight/{user_id}")
        if response.status_code == 200 :
            print("✅ [Global Model Test] Berhasil menghapus parameter classifier global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal menghapus parameter classifier global model ")
        raise Exception
    
    def test_model_update_for_admin(self):
        # Implementasikan pengujian untuk pembaruan model global jika diperlukan
        response = self.admin_request("GET", f"model/update")
        if response.status_code == 200 :
            print("✅ [Global Model Test] Berhasil mengupdate model global ")
            return
        else :
            print("❌ [Global Model Test] Gagal mengupdate model global ")
        raise Exception
    
    def test_model_update_for_user(self):
        response = self.request("GET", f"model/update")
        if response.status_code == 403 :
            print("✅ [Global Model Test] Berhasil mencegah user mengupdate model global ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user mengupdate model global ")
        raise Exception
    
    def test_delete_training_data_for_admin(self, weight_id : str):
        response = self.admin_request("DELETE", f"training/{weight_id}")
        if response.status_code == 200 :
            print("✅ [Global Model Test] Berhasil menghapus data bobot global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal menghapus data bobot global model ")
        raise Exception
    
    def test_delete_training_data_for_user(self, weight_id : str):  
        response = self.request("DELETE", f"training/{weight_id}")
        if response.status_code == 403 :
            print("✅ [Global Model Test] Berhasil mencegah user menghapus data bobot global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user menghapus data bobot global model ")
        raise Exception
    
    def test_delete_model_weight_for_admin(self, weight_id : str):
        response = self.admin_request("DELETE", f"model/weights/{weight_id}")
        if response.status_code == 200 :
            print("✅ [Global Model Test] Berhasil menghapus data bobot global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal menghapus data bobot global model ")
        raise Exception
    
    def test_delete_model_weight_for_user(self, weight_id : str):
        response = self.request("DELETE", f"model/weights/{weight_id}")
        if response.status_code == 403 :
            print("✅ [Global Model Test] Berhasil mencegah user menghapus data bobot global model ")
            return
        else :
            print("❌ [Global Model Test] Gagal mencegah user menghapus data bobot global model ")
        raise Exception
    
    
    def test_add_model_weight(self):
        payload = {
            
        }

        with open("data/TrainingWeight.json", "r") as f:
            payload = json.load(f)

        response = self.request("POST", "model/weights", payload=payload)
        
        if response.status_code == 201 :
            print("✅ [Global Model Test] Berhasil menambahkan data bobot global model ")
            data = response.json()["data"]
            self.test_delete_training_data_for_user(data["training_id"])
            self.test_delete_training_data_for_admin(data["training_id"])
            self.test_delete_model_weight_for_user(data["weight_id"])
            self.test_delete_model_weight_for_admin(data["weight_id"])
            return
        else :
            print("❌ [Global Model Test] Gagal menambahkan data bobot global model ")
        raise Exception