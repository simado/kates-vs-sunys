# Katė ar Šuo
## Prieš pradedant

Projektas yra skirtas daugiau išmokti apie TensorFlow ir Keras bibliotekas.

Projektas buvo atliktas sekant mokomąja medžiagia iš YouTube: [Deep Learning with Python, TensorFlow, and Keras tutorial](https://www.youtube.com/watch?v=j-3vuBynnOE&feature=emb_title).

Projekte naudoti duomenys: 60,000 nuotraukų rinkinys, kuriame yra:
- 30,000 šunų nuotraukų
- 30,000 kačių nuotraukų

Duomenys yra pasiekiami per [šią nuorodą](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765)

## Reikalingos bibliotekos

Kuriant CNN modelį buvo naudota [Google Colab](https://colab.research.google.com/) ir Jupyter Notebook. Šias knygas galima rasti [notebooks](https://github.com/simado/kates-vs-sunys/tree/master/notebooks) aplankale.

Toliau, buvo planuota patalpinti veikianti modelį online ir pasiekiamą vartotojui, todėl buvo sukurtas **web app** atliekantis reikalingus veiksmus ant **localhost** ir esantis `app.py`faile. Tačiau nors viskas sėkmingai veikė asmeniniame kompiuteryje, iškilo daugybė problemų bandant perkelti tai į tokias hostinimo platformas kaip:
- [Heroku](www.heroku.com)
- [PythonAnywhere](www.pythonanywhere.com)

Taip pat buvo planų naudoti AWS, tačiau nepavyko rasti tokio būdo kuris būtų visiškai nemokamas.

Kuriant `app.py` naudojau **Conda** virtualią aplinką ir naudojau šias bibliotekas:
```
numpy
flask
wtforms
tensorflow
opencv-python
urllib.request
```
Taip pat yra pridedamas `requirements.txt` dokumentas su sarašu visų bibliotekų.
