import pytest
import pytest_check as check
import Models as Ms


@pytest.mark.incremental
class TestGenOpt:

    @pytest.mark.full_scenery
    def test_create_model_group(self, client):
        """
        Create group of models with GraphQL endpoint
        """
        request = Ms.GroupOfModelRequest(client.group)
        response = client.post_gql_request(query=request.query, variables=request.variables)
        response.assert_status_code(200).validate(Ms.GroupOfModelResponse)

    @pytest.mark.full_scenery
    def test_create_models(self, client):
        for model in client.group.MODEL.__dict__.values():
            request = Ms.ModelRequest(model, client.group)
            response = client.post_gql_request(query=request.query, variables=request.variables)
            response.assert_status_code(200).validate(Ms.ModelResponse)
        check.equal(1, 1)
        check.equal(1, 2)
        check.equal(1, 1)
        check.equal(1, 3)
        check.equal(1, 4)
        check.equal(1, 6)
        if check.any_failures():
            # only check these if the above passed
            raise AssertionError

    @pytest.mark.full_scenery
    def test_upload_tr(self, client):
        request = Ms.UploadTRRequest(client.group)
        file = open("05_Ц1_ТР_НЕФТЯНЫХ_НА_МАЙ_2023г без пароля [N92oDN].xlsx", "rb")
        response = client.upload_file(file=file, params=request.params, data=request.form_data)
        response.assert_status_code(200).validate(Ms.ModelResponse)
        # response = client.post_gql_request(query=Ms.GroupOfModelRequest.query, variables=Ms.GroupOfModelRequest.variables)
        # response_obj = Response(response)
        # response_obj.assert_status_code(200).validate(Ms.GroupOfModelResponse)
