# Sumario:
- [^0]: Gerenciamento_de_Versão:
- [^1]: Comandos_Basicos:
    - [^2]: Operações_com_Arquivos
    - [^3]: Commit
    - [^4]: Diff
    - [^5]: Show 
    - [^6]: Remover
    - [^7]: Clean
    - [^8]: Observar_arquivo
    - [^9]: Reset
    - [^10]: Tag
- [^11]: Branchs:
- [^12]: Operações_de_Repositorios_Remot:os:
- [^13]: Contribuição,_Gitflow:
- [^14]: Uso:

# Gerenciamento de Versão :[^0]

Major.Minor.Patch

Incremento          | Descrição                       
:-------------------| :----------:                    
Major               |Quebra de funcionalidade    
Minor               |Nova Feature                
Patch               |Concerto+Qualquer outra coisa                    



# Comandos Basicos[^1]

> Iniciar Repositorio
~~~bash
    git init
~~~

> Checa o status do projeto, o que foi e não foi modificado e o status dos arquivos que estão sendo observados

~~~bash
    git status
~~~

> Para ver as mensagens de commits

~~~bash
    git log
~~~

> Mostra um registro de todas as mudanças feitas para o cabeçalho repositorio local

~~~bash
git reflog
~~~

## Operações com Arquivos[^2]

> Adicionar uma Arquivo
~~~bash
    git add "nome_do_arquivo"
~~~

> Adicionar todos os Arquivos
~~~bash
    git add .
~~~

> Para mover ou renomear arquivo
~~~bash
    git mv <old_file> <new_file>
~~~

> Para recuperar alterações de um arquivo, ou versões passadas dele, use:
> você pode conseguir esse número usando "git log"

~~~bash
    git checkout "numero_da_modificação" -- "nome_do_arquivo"
~~~

## Commit[^3]

> Adicionar uma mensagem ao commit
~~~bash
    git commit -m "mensagem"
~~~

> Para modificar a mensagem do ultimo commit:

~~~bash
    git commit "mensagem" --amend
~~~

> Para modificar o conteudo do ultimo commit, adicionando novo conteudo, mas sem ter que criar um novo commit:

~~~bash
    git commit --amend --no-edit
~~~

> Criar um commit que desfaz um commit anterior

~~~bash
    git revert "commit_id"
~~~



## Diff[^4]

> Para mostrar as diferenças
~~~bash
    git diff
~~~

> Para mostrar a diferenã entre dois commits
~~~bash
git diff <commit_id1>..<commit_id2>
~~~

## Show [^5]

> E para só ver a ultima modificação use:

~~~bash
    git show
~~~

> Para ver as modificações feitas em um arquivo, use:
~~~bash
    git show "numero_da_modificaçãos"
~~~

## Remover[^6]

> Para remover o arquivo da arvore de trabalho
~~~bash
    git rm "nome_do_arq"
~~~

> Para remover um arquivo que foi removido mas ainda está operando
~~~bash
    git rm --cached <file_name>
~~~

> Remover pasta do projeto git
~~~bash
    git rm -rf --cached folder1/
~~~
## Clean[^7]

> Serve para limpar o repositorio dos varios arquivos que um build ou coisa do tipo podem criar:

> O paretro -n irá mostrar os arquivos que vão ser apagados
> O paretro -f irá de fato apagar os arquivos

~~~bash
    git clean -n
    git clean -f
~~~

## Observar arquivo[^8]

> Para assumir que um arquivo não é modificado
~~~bash
git update-index --assume-unchanged "arquivo"
~~~

> Para voltar a monitorar modificações
~~~bash
git update-index --assume-unchanged "arquivo"
~~~

## Reset[^9]


> Para remover uma arquivo que sem querer foi dado `add` nele
~~~bash
git reset -- Nome_do_arquivo
~~~

> Discartar todas as alterações já feitas e mover o cabeçalho para um commit especifico
~~~bash
git reset --hard <commit_id>
~~~

> Move o cabeçalho para um commit especifico mas preserva as mudanças feitas
~~~bash
git reset --soft <commit_id>
~~~
> Move o cabeçalho para um numero de commits atras, mas preservando as mudanças feitas
~~~bash
git reset --soft <commit_id> HEAD~int
~~~

## Tag[^10]
> Lista todas as tags do projeto
~~~bash
git tag
~~~
> Cria uma tag apontando pro ultimo commit feito
~~~bash
git tag nome_tag

git tag nome_tag -m "mensagem que acompanha a tag"
~~~
> Lista todas as tags e suas descrições
~~~bash
git tag -n
~~~
> Pra mandar um tag pro repositorio usa:
~~~bash
git push origin nome_tag
# manga todas as tags
git push origin --tag
~~~

# Branchs[^11]

> Para ver todas as branch que existem no projeto, use:
~~~bash
    git branch
~~~
> Para criar ramificações(branchs) do código, use:
~~~bash
    git branch "nome_da_branch_nova"
~~~

> Para deletar uma branch, use:
~~~bash
    git branch -D "nome_da_branch"
~~~

> Para listar todas as branchs remotas
~~~bash
    git branch -r
~~~
> Para mudar da branch principal para outra, use:
~~~bash
    git checkout "nome_da_branch"
~~~

> Para unir o conteudo das branch, use:
~~~bash
    git merge "nome_da_branch"
~~~

> Cancelar o marge em caso de conflito
~~~bash
    git merge --abort
~~~

# Operações de Repositorios Remotos[^12]

> Para listar os repositorios remotos

~~~bash
    git remote
~~~

> Para adicionar um repositorio remoto

~~~bash
    git remote add "nome" "url"
~~~

> Para mandar o repositório para o github, use:
~~~bash
    git push
~~~
> Caso seja a primeira vez que manda algo para o repositório, use:
~~~bash
    git push -u origin master
~~~
> Para clonar um projeto já iniciado, use:
~~~bash
    git clone "url_do_repositório"
~~~
> Para trazer as alterações do repositório para o projeto, use:
~~~bash
    git pull
~~~
> para trazer as alterações do repositorio, mas os commits que form pegos do repositorio vão estar sendo colocados na fila, atras dos meu no repo local
~~~bash
    git pull --rebase
~~~
> Para poder fazer um rebase, mas sem a necessidade de comitar o que você fez até o momento, você pode fazer o stash, que guarda em separado suas auteraçoes, para que você possa depois de fazer o rebase, aplicar elas denovo
~~~bash
    # Remove e guarda as alterações já feitas
    git stash
    # Lista as alterações armazenadas 
    git stash list
    # Reaplica as ultimas alterações guardas no stash
    git stash pop
~~~

> Para trazer as alterações do repositório para o projeto, use:
~~~bash
    git pull <remote_name> <remote_branch>
~~~

# Contribuição, Gitflow[^13]

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

# Uso[^14]

> Para iniciar o uso de gitflow
~~~bash
    git flow init 
~~~
> Depois você nomeia as branches
> Para adicionar feature
~~~bash
    git flow feature start nova-funcao
~~~
> Para fazer o merge na develop 
~~~bash
    git flow feature finish sum
~~~
> Para fazer uma release
~~~bash
    git flow release start 0.1.0
~~~
> Para mandar a release para a master
~~~bash
    git flow release finish 0.1.0
~~~