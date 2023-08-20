import pytest
import Models as Ms


@pytest.mark.incremental
class TestGenOpt:

    @pytest.mark.full_scenery
    def test_create_model_group(self, client):
        request = Ms.GroupOfModelRequest(client.group)
        response = client.post_gql_request(query=request.query, variables=request.variables)
        response.assert_status_code(200).validate(Ms.GroupOfModelResponse)

    @pytest.mark.full_scenery
    def test_create_models(self, client):
        for model in client.group.MODEL.__dict__.values():
            request = Ms.ModelRequest(model, client.group)
            response = client.post_gql_request(query=request.query, variables=request.variables)
            response.assert_status_code(200).validate(Ms.ModelResponse)

    @pytest.mark.full_scenery
    def test_upload_tr(self, client):
        request = Ms.UploadTRRequest(client.group)
        file = open("../02_Ц1_ТР_НЕФТЯНЫХ_НА_ФЕВРАЛЬ_2022г на печать (2) (2).xlsx", "rb").read()
        response = client.upload_file(file=file, params=request.params)
        response.assert_status_code(200).validate(Ms.ModelResponse)
        # response = client.post_gql_request(query=Ms.GroupOfModelRequest.query, variables=Ms.GroupOfModelRequest.variables)
        # response_obj = Response(response)
        # response_obj.assert_status_code(200).validate(Ms.GroupOfModelResponse)
