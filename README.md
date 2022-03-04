# Demo CD 

## Présentation 

Ce projet a pour but de mettre en place un système de CD pour le déploiemnet d'une application python sur Azure.

## Utilisation 
### Repo GIT
- git branch : s'assurer d'etre sur la main
- git pull  <br> <br>
- git checkout dev
- Faire les modifs
- git add .
- git commit -m "fix/feat/chores/docs: ..."
- git push  <br> <br>
- git checkout main
- git merge dev
- git push

### Azure
- Créer Registre de conteneurs

#### Azure-Cli
- choco install azure-cli
- az login
- az acr login --name [my-registry-name] <br> <br>
- commande qui génère un JSON avec les credentials nécessaires aux applications afin de se connecter aux ressources : 
- az ad sp  create-for-rbac --name "demo" --role contributor --scope /subscriptions/[ID-dabonnement]/resourceGroups/[nom-du-groupe-de-resource] --sdk-auth
- enregistrer l'output dans les Actions Secrets de Github (REGISTRY_USERNAME, REGISTRY_PASSWORD, AZURE_CREDENTIALS)


### Docker
- docker build . -t [nom-image]:[tag] 
- docker tag [nom-image]:[tag] [nom-serveur-azure]/[nom-image]:[tag]
- docker push [nom-serveur-azure]/[nom-image]:[tag] <br> <br>

- Une fois les Action Secrets entrés et docker push réussi, on peut vérifier si l'image est en ligne :
- docker pull [nom-serveur-azure]/[nom-repo]

### Action Secrets sur GitHub
- REGISTRY_LOGIN_SERVER : [nom-serveur-connexion-azure]
- REGISTRY_USERNAME : [clientId]
- REGISTRY_PASSWORD : [clientSecret]
- AZURE_CREDENTIALS : [credentials-generés-par-la-grosse-commande]


## Liens Utiles 
