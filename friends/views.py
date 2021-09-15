# from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from friends.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'MESSAGE':'CREATED OK'}, status=201)


    def get(self, request):
        owners = Owner.objects.all()
        with_my_dog = []

        for owner in owners:
            # 역참조 데이터 얻기: 테이블명소문자_set
            dogs = owner.dog_set.all()
            dog_list = []
            for dog in dogs:
                dog_list.append(
                    {
                        "a_name" : dog.name,
                        "b_age" : dog.age
                    }
                )
            with_my_dog.append(
                {
                    "a_name": owner.name,
                    "b_age": owner.age,
                    "c_email": owner.email,
                    "d_dog_list": dog_list
                } 
            )
        return JsonResponse({"results": with_my_dog}, status=200)


class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner'])

        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = owner
        )
        return JsonResponse({'MESSAGE':'CREATED OK'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            dog_info = {
                "name": dog.name,
                "age": dog.age,
                "owner": dog.owner.name
                # 아래의 경우도 되는데 이렇게 할 필요가 없었다. medles에서 Owner를 ForeinKey로 설정한 코드 때문인 것 같다.
                # dog.owners.name로 value를 지정하면 안되는 것을 보니 거의 확실한 것 같다.
                # "owner": Owner.objects.get(id=dog.owner_id).name,
            }
            results.append(dog_info)
        return JsonResponse({"results":results}, status=200)