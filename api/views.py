from django.core.exceptions import ObjectDoesNotExist

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response

from .models import Organization
from .serializers import OrganizationSerializer
from .integrations.github import GithubApi

from django.conf.urls import url

schema_view = get_swagger_view(title='Pastebin API')

class OrganizationViewSet(ModelViewSet):

    queryset = Organization.objects.all().order_by('-score')
    serializer_class = OrganizationSerializer
    lookup_field = "login"


    def retrieve(self, request, login=None):
        """Recupera a organização passada no parâmetro caso ela exista na api do 
            Github.

        :login: login da organização no Github
        """
        try:
            org = Organization.objects.get(login=login)
            serializer_response = OrganizationSerializer(org)

            return Response(serializer_response.data)
        except ObjectDoesNotExist:
            github = GithubApi()
            new_org, response_code = github.get_organization(login)
            new_org_members = github.get_organization_public_members(login)

            if response_code == 200:
                count_members = len(new_org_members)
                score = int(new_org['public_repos']) + count_members

                org_response = Organization.objects.create(
                    login=login,
                    name=new_org['name'],
                    score=score
                )
                serializer_response = OrganizationSerializer(org_response)

                return Response(serializer_response.data)

            return Response(status=404)

    def list(self, request):
        """Lista todas as organizações já recuperadas pela API.

        """
        queryset = Organization.objects.all().order_by('-score')
        serializer_response = OrganizationSerializer(queryset, many=True)
        return Response(serializer_response.data)


    def destroy(self, request, login=None):
        """Apaga do cache a organização passada no parâmetro caso ela exista na api do 
            Github.

        :login: login da organização no Github
        """
        try:
            org = Organization.objects.get(login=login)
            org.delete()

            return Response(status=204)
        except ObjectDoesNotExist:
            return Response(status=404)
