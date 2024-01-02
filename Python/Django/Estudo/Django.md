# Sumario [^0]

- [^0]: Sumario
- [^1]: Django_Projeto
- [^2]: Configuração_do_Banco_de_dados
- [^3]: Modelos
- [^4]: APPS
- [^5]: Passagem_de_Argumento_por_URL
- [^6]: Views_Genericas
- [^7]: Test
- [^8]: Arquivos_Estáticos

# Django Projeto [^1]

[^0]:Sumario

Para criar um projeto/app
~~~
django-admin startproject nome_do_projeto
~~~

Evitar nome que podem calsar conflito com pacotes do django ou python

O `magage.py` é um utilitário de linha de comando com qual você vai interagir com o projeto

o diretorio `nome_do_projeto/` interior é um pacote de onde se importa coisa que se vai usar como `nome_do_projeto.urls`

em `nome_do_projeto/urls.py` vão estar as configurações de rota do projeto djangle

em `nome_do_projeto/settings.py` vão estar as configurações do projeto como um todo Django

para executar o projeto:

~~~zsh
 python manage.py runserver
~~~

Para escolher o ip e a porta

~~~bash
python manage.py runserver 8080
# ou
python manage.py runserver 0.0.0.0:8000
~~~

Para criar um app dentro do projeto:

~~~
python manage.py startapp app_name
~~~

A função `path()` é passado quatro argumentos, 
    	dois obrigatórios: `route` e `view` 
    	dois opcionais: `kwargs`, e `name`

> `Route` é uma string contendo uma descrição de url
>
> `view` é chamada depois de route com uma requisição Httprequest
>
> `kwargs` Argumentos nomeados arbitrariamente que podem ser passados em um dicionario para a view objetivada
>
> `name` Serve pra nomear uma url para que ela possa ser chamada de qualquer logar no Django, em especial em templates

# Configuração do Banco de dados [^2]

[^0]:Sumario

O Django usa por padrão o sqlite3 como banco de dados, mas ele pode ser alterado facilmente antes de ir pra produção modificando parametros dentro de `DATABASES.['default']`, mas especificamente `ENGINE` e `NAME`, e outros campos que devem ser criados como `USER`,`PASSWORD` e `HOSTNAME`

# Modelos [^3]

[^0]:Sumario

Os modelos são classes derivadas da classes `django.db.modeles.Model` e cada modelo possui alguns atributos de classes, os quais vão representar campos no banco de dados do modelo

Um exemplo de modelo é:

~~~python
    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
        def __str__(self):
            return self.choice_text
~~~

Cada campos é representado por uma instancia __Field__ ex: __CharField__ 

~~~
question = models.ForeignKey(Question, on_delete=models.CASCADE)
~~~

O primeiro campo do __Field__ é preenchivel com um nome que pode possa ser legivel pra humanos, mas caso não seja preenchido, ele será definido pela maquina

# APPS [^4]

[^0]:Sumario

Ainda em `settings.py`, em `INSTALLED_APPS`, haverá uma lista de aplicações presentes no projeto, que podem tanto serem empacotadas e usadas em outro projeto casa seja de seus desejo

Alguns apps que vem por padrão precisam de tabelas no banco de dados, e pra usa-las, deve se roda o comando:

~~~
python manage.py migrate
~~~

Caso não sinta a necessidade de usar um app presente na lista, só comente ou apague a linha dele e rode a migração

## APP e Migrations

[^0]:Sumario

Para adicinar um App em nosso prjeto, nos temos que em `INSTALLED_APPS` adicinar o caminho ate a classe *Config dentro de apps
~~~
"polls.apps.PollsConfig"
~~~

com isso se rodarmos a migration:

~~~
python manage.py makemigrations polls
~~~

Vamos criar uma migration com as tabelas no banco de dados que fazem referencia ao modelo que criamos

E com :

~~~
python manage.py sqlmigrate polls 0001 
~~~

executamos aquele modelo

E por fim se executa :

```
python manage.py migrate
```

Que ira aplicar as migrações que ainda não foram feitas

Em suma o processo se consiste em:

- Alterar os  modelos (em `models.py`).
- Rodar `python manage.py makemigrations` para criar migrações para suas modificações
- Rodar `python manage.py migrate` para aplicar suas modificações no banco de dados.

## APP shell

[^0]:Sumario

Podemos usar um shell interativo pra manipular o banco de dados

~~~
python manage.py shell
~~~

fazemos desse jeito pra que junto ao shell python, também seja carregado as configurações de `manage.py`

~~~python
from polls.models import Choice, Question  
# Import the model classes we just wrote.

# No questions are in the system yet.
Question
# Como os itens retornados são objetos Python Question, é interessante ser definido um __str__() pras classes pra uma mais facil leitura delas
#  <QuerySet [todos os objetos registrados na tabela Questions]>

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
# Com isso agente consegue fazer um novo registro na tabela Questions
q.save()
# Salvamos aterações
q.question_text # Irá exibir o texto
q.question_text="Não use drogas" # Irá mudar o texto
q.save() # Salva alteração

# Podemos procurar dados:
Question.objects.filter(id=1) #id
Question.objects.filter(question_text__startswith="What") # texto
# Por ano
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

from polls.models import Choice, Question

# Make sure our __str__() addition worked.
Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
from django.utils import timezone
>>> current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
q = Question.objects.get(pk=1)
q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
q.choice_set.all()
<QuerySet []>

# Create three choices.
q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=current_year)
#<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()

~~~

## APP ADMIM

[^0]:Sumario

Os sites tem adiminstradores que podem escrever e deletar conteudo, e o comando pra criar um adm é :

~~~bash
python manage.py createsuperuser  
~~~

E depois de preencher os dados, você ja vai ser capaz de logar na pagina

É possivel no arquivo `setting.py` alterar a linguagem do site atraves do parametro `LANGUAGE_CODE`

Como é visivel vistando o adimin, as informações de tabela e tals, relacionadas a `Questions` não é visivel, e para isso é necessario importa-la dentro de `polls/admin.py` para que isso seja possivel:

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

### Configuração de Tabelas em Admin

É possível configurar os campos na área de administrador usando

~~~python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
~~~

Isso é útil pra organizar os campos na tabela de forma que seja mais simple e legivel a que está preenchendo eles, principalmente quando se tem muitos dados pra preencher

~~~py
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
~~~

Por exemplo, usando:

~~~python
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
   
admin.site.register(Question, QuestionAdmin)
~~~

É possível ligar um formulário ao outro, e definir quantos campos ele vai ter de padrão, além de uma opção de adicionar outros campos.

Pra lidar com situação onde não é muito grande a tambéla, tem:

~~~python
class ChoiceInline(admin.TabularInline):
    ...
~~~

### Personalize a listagem da página de Admin

O Django de padrão usa o `__str()__` pra exibir as tabelas registradas, e o `list_display` permite exibir os valores da tabela o invez disso:

~~~python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date"]
~~~

Além disso, é possivel adicionar um filtro e dizer que parametros serão usados como filtro usando:

~~~python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_filter = ["pub_date"]
~~~

Isso irá criar um filtro por data, ou adpender do tipo de campo

Ou para criar um campo e busca por texto, e usa internamente uma consulta `LIKE`

~~~python
class QuestionAdmin(admin.ModelAdmin):
    # ...
	search_fields = ["question_text"]
~~~

### Modificar a Área de Adimin

Para modificar a área de admin, é feito adicionando um valores em uma lista em `settings.py`, onde vamos configurar um template. __DIRS__ é uma lista de diretorios que o Django checa quando vai atrás dos templates:

~~~python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
~~~

# Passagem de Argumento por Url [^5]

[^0]:Sumario

Em Urls você vai ter:

~~~python
path("<int:question_id>/vote/", views.vote, name="vote"),
# <conversor:nome_de_variavel_passado_pra_view>
~~~

Em Views você vai ter:

~~~python
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
~~~

A View não se limita a entrevar htmls ou coisa do tipo, ela pode ser usada pra envira arquivos, gerar arquivos, baixar aquivos, a unica coisa que o Django espera é que haja um `HttpResponse` ou uma exessão

Com:

~~~py
from django.http import HttpResponse
# Importa do banco a tabela Question e seus valores são objetos dentro de uma lista Question=[{:},{:},...]
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ",<br> ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
~~~

O problema dessa abordagem é que limita como agente pode usar e produzir paginas

E pra resolver isso usamos templates, os quais devem estar em uma pasta chamada templates dentro da pasta do App, isso é configurado por `TEMPLATES` em `settings.py`, o diretorio fica, `polls/templates/polls/index.html`

E apesar disso, porcausa do `app_directories`, no Django você vai se referir a ele como `polls/index.html`

Nessa situação, o uso de um subdiretorio a templates `templates/polls/index.html` serve pra evitar que o Django confunda  o `index.html` de polls com o de outra aplicação

Então, vamos ter:

~~~py
from django.http import HttpResponse
from .models import Question
from django.template import loader 

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list,}
    return HttpResponse(template.render(context, request))
~~~

Dado o quão comum é esse processo e padrão de escrita de uma reposta, existe o atalho `render` :

~~~python
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
~~~

e no `index.html`

~~~django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
~~~

Esse processo faz a chamada do template `polls/index.html` e passa para ele um contexto que é um set de dicionarios mapeando os valores  do banco, e para usar o contexto passado como variaviavel, ela deve estar entre `{{variavel}}`

Para escrever um `for` em Django e estrutura é :

~~~django
{% for paragraph in text %}
	<p>{{paragraph}}</p>
{% endfor %}
~~~

Para escrever um `if` em Django e estrutura é :

~~~django
{% if valor %}
    # test true
{% else %}
	# test false
{% endif %}
~~~

Caso haja a possibilidade de uma pagina buscada não existir, usa-se

`polls/views.py`

```py
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

ou de uma forma mais consisa

~~~py
from django.shortcuts import get_object_or_404, render
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
~~~

## Get Objetct e Get List

[^0]:Sumario

`get_object_or_404` : Se os dados procurados não existirem em Question, é retornando um 404
`get_list_or_404` : funciona como get_object, com a diferença de que 'object' faz um get no banco, enquanto 'list' faz um filter

## Alterando Urls

[^0]:Sumario

Ao definirmos urls, corremos o risco de ter que corrigir ou alterar elas caso algo ou um caminho no codigo mude, por isso, há meios para evitar isso, por meio das definições que fizemos no arquivo `polls.urls`

~~~django
# Ao invez de fazermos isso:
<a href="/polls/{{ question.id }}/">
# Fazemos
<a href="{% url 'detail' question.id %}">
~~~

E pra uma questão de uma aplicação que tem varios outros app que usam a mesma `name` como no caso acima `detail`, pra isso usamos uma variavel chamada `app_name` que fica em `urls.py`

~~~py
#polls/urls.py
#...
app_name = "polls"
#...
~~~

E no html vamos usar:

~~~django
# Não isso
<a href="{% url 'detail' question.id %}">
# Mas isso
<a href="{% url 'polls:detail' question.id %}">
~~~

## Formulario Django

[^0]:Sumario

~~~django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
~~~

## csrf_token

[^0]:Sumario

O marcador abaix serve pra gerar um csrf token pra ajudar acombater esse tipo de ataque

~~~django
{% csrf_token %}
~~~

Form:

~~~django
<form action="{% url 'polls:vote' question.id %}" method="post">
~~~

A configuração em questão permite atraves das seguintes informações fazer uma requisição pra: 'polls/vote/id'

~~~python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
~~~

- `request.POST` é um objeto que permite acessar os valores submetidos(os valores passados sempre são strings) ha também `request.GET`
- Além disso, o `HttpResponseRedirect` serve pra que ao fim da submição o usuario seja redirecionado pra evitar multiplas submições
- O `reverse` em questão ele vai servir pra construir e direcionar o usuario pra uma nova url que vai ser construida com base nos parametros passados

# Views Genericas [^6]

[^0]:Sumario

O Django vai dar a possibilidade do uso de Views generica com as quais você pode abstrair todoo codigo trabalhoso anteriomente feito

~~~py
# index view
class IndexView(generic.ListView):
    # aponta template
    template_name = "polls/index.html"
    # aponta variavel de contexto
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
# A nova detail view
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
~~~

# Test [^7]

[^0]:Sumario

São criados atraves de uma subclasse Django e colocados no arquivo de tests.py da aplicação

~~~py
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
     def test_was_published_recently_with_old_question(self):
		pass

     def test_was_published_recently_with_recent_question(self):
     	pass
~~~

E pra executar os testes usamos 

~~~bash
python manage.py test polls
~~~

 E como mostrado acima, há o teste se do metodos publica rentemente do modelo Question

Nos também podedmos fazer testes que dizem respeito ao Client site pormeio de:

~~~
python manage.py shell
~~~

~~~py
from django.test.utils import setup_test_environment
setup_test_environment()
~~~

~~~py
from django.test import Client
# Cria um instancia do cliente
client = Client()
# Para obter reposta de '/'
response = client.get("/") # Not Found 

response.status_code # 404

#Nos iremos usar 'reverse()' ao invez da url hardcoded
from django.urls import reverse

response = client.get(reverse("polls:index"))

response.status_code # 200

response.content # b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'

response.context["latest_question_list"] # <QuerySet [<Question: What's up?>]>
~~~

Boas práticas de testes incluem ter:

- um “TestClass” separado para cada modelo ou view
- um método de teste separado para cada conjunto de condições que você quer testar
- nomes de métodos de teste que descrevem a sua função

# Arquivos Estaticos [^8]

[^0]:Sumario

São arquivos como imagens, css, e JS

Eles devem ser colocados no diretorio `polls/static/polls/*` e o Django vai encontrar eles assim como encontra os templates

Então criamos por exemplo um arquivo `style.css` dentro dele e no `*.html`

~~~django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/styles.css' %}">
~~~

E por exemplo, se formos referenciar uma imagem dentro de `static/polls`, simplesmente fazemos 

```css
body {
    background: white url("images/background.png") no-repeat;
}
```

E dessa forma, mesmo que a pasta img for mudada de local, basta reconfigurar o Static e tudo será reolvido