from django.shortcuts import render
def index(request):
    objects_array = [
        {
            "id": "1",
            "title": "Товар 1",
            "vendor_code": "VC111",
            "description": "Описание 1",
            "price": 100,
            "img": "/images/uso_001.jpg"
        },
        {
            "id": "2",
            "title": "Товар 2",
            "vendor_code": "VC222",
            "description": "Описание 2",
            "price": 200,
            "img": "/images/uso_002.jpg"
        },
        {
            "id": "3",
            "title": "Товар 3",
            "vendor_code": "VC333",
            "description": "Описание 3",
            "price": 300,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg"
        },
        {
            "id": "4",
            "title": "Товар 4",
            "vendor_code": "VC444",
            "description": "Описание 4",
            "price": 400,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg"
        }
    ]
    return render(request, "shop/index.html", context={"objects_array": objects_array})
