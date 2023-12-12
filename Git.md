# Comandos Basicos

> Iniciar Repositorio
~~~
    git init
~~~

> Checa o status do projeto, o que foi e não foi modificado e o status dos arquivos que estão sendo observados

~~~
    git status
~~~

> Para ver as mensagens de commits

~~~
    git log
~~~

> Mostra um registro de todas as mudanças feitas para o cabeçalho repositorio local

~~~
git reflog
~~~

## Operações com Arquivos

> Adicionar uma Arquivo
~~~
    git add "nome_do_arquivo"
~~~

> Adicionar todos os Arquivos
~~~
    git add .
~~~

> Para mover ou renomear arquivo
~~~
    git mv <old_file> <new_file>
~~~

> Para recuperar alterações de um arquivo, ou versões passadas dele, use:
> você pode conseguir esse número usando "git log"

~~~
    git checkout "numero_da_modificação" -- "nome_do_arquivo"
~~~

## Commit

> Adicionar uma mensagem ao commit
~~~
    git commit -m "mensagem"
~~~

> Para modificar a mensagem do ultimo commit:

~~~
    git commit "mensagem" --amend
~~~

> Criar um commit que desfaz um commit anterior

~~~
    git revert "commit_id"
~~~
> Para você ver os arquivos que foram modificados, que estão sendo observados pelo git use:

## Diff

> Para mostrar as diferenças
~~~
    git diff
~~~

> Para mostrar a diferenã entre dois commits
~~~
git diff <commit_id1>..<commit_id2>
~~~

## Show 

> E para só ver a ultima modificação use:

~~~
    git show
~~~

> Para ver as modificações feitas em um arquivo, use:
~~~
    git show "numero_da_modificaçãos"
~~~

## Remover

> Para remover o arquivo da arvore de trabalho
~~~
    git rm "nome_do_arq"
~~~

> Para remover um arquivo que foi removido mas ainda está operando
~~~
    git rm --cached <file_name>
~~~

> Remover pasta do projeto git
~~~
    git rm -rf --cached folder1/
~~~
## Observar arquivo

> Para assumir que um arquivo não é modificado
~~~
git update-index --assume-unchanged "arquivo"
~~~

> Para voltar a monitorar modificações
~~~
git update-index --assume-unchanged "arquivo"
~~~

## Reset

> Discartar mudanças e mover o cabeçalho para um commit especifico
~~~
git reset --hard <commit_id>
~~~

> Move o cabeçalho para um commit especifico mas preserva as mudanças feitas
~~~
git reset --soft <commit_id>
~~~

# Branchs

> Para ver todas as branch que existem no projeto, use:
~~~
    git branch
~~~
> Para criar ramificações(branchs) do código, use:
~~~
    git branch "nome_da_branch_nova"
~~~

> Para deletar uma branch, use:
~~~
    git branch -D "nome_da_branch"
~~~

> Para listar todas as branchs remotas
~~~
    git branch -r
~~~
> Para mudar da branch principal para outra, use:
~~~
    git checkout "nome_da_branch"
~~~

> Para unir o conteudo das branch, use:
~~~
    git merge "nome_da_branch"
~~~

> Cancelar o marge em caso de conflito
~~~
    git merge --abort
~~~

# Operações de Repositorios Remotos

> Para listar os repositorios remotos

~~~
    git remote
~~~

> Para adicionar um repositorio remoto

~~~
    git remote add "nome" "url"
~~~

> Para mandar o repositório para o github, use:
~~~
    git push
~~~
> Caso seja a primeira vez que manda algo para o repositório, use:
~~~
    git push -u origin master
~~~
> Para clonar um projeto já iniciado, use:
~~~
    git clone "url_do_repositório"
~~~
> Para trazer as alterações do repositório para o projeto, use:
~~~
    git pull
~~~

> Para trazer as alterações do repositório para o projeto, use:
~~~
    git pull <remote_name> <remote_branch>
~~~

# Contribuição, Gitflow

- pra resolver problemas é criado uma branch

- Pode se separar o git flow em 2 tipos de branchs

1. Branches principais
    - Master 
    - Developer
1. Branches de Suporte
    - Feature
    - Release
    - Hotfix

## Aplicação

- Master: é usada para mandar os commit dos release para produção
- Develop: é criada apartir da Maste e conterá as fetures estaveis que seram mergeadas em uma branche de release
- Features: É criada através da Develop

- Nomeação de branch
    > feature/nova-feature

## Ciclo de vida

### Feature

Master[1.0] -> Develop -> Feature -> Develop -> Release -> Master[2.0]

### Hotfix

Master[2.0] -> Hotfix -> Master[2.1]

# Uso

> Para iniciar o uso de gitflow
~~~
    git flow init 
~~~
> Depois você nomeia as branches
> Para adicionar feature
~~~
    git flow feature start nova-funcao
~~~
> Para fazer o merge na develop 
~~~
    git flow feature finish sum
~~~
> Para fazer uma release
~~~
    git flow release start 0.1.0
~~~
> Para mandar a release para a master
~~~
    git flow release finish 0.1.0
~~~