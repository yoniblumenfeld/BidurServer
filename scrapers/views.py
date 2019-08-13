from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # <-- Here

from scrapers.db import db_queries

class ScrapersData(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request,format=None):
        params = self.request.query_params
        keywords_list = (params[key] for key in params.keys() if key.startswith('key'))
        results = db_queries.search_db_for_keywords(keywords_list)
        return Response({'results':results})
