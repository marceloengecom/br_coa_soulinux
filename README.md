## Plano de Contas Odoo - Modelo SOULinux 
 

### PROCEDIMENTO DE INSTALAÇÃO

#### Confira se você tem a pasta de módulos customizados "custom-addon":

Ex: ls /opt/odoo/custom-addons


#### Crie uma subpasta. Ex: 'soulinux'

Ex: mkdir /opt/odoo/custom-addons/soulinux


#### Acesse a respetiva pasta e faça um git clone do repositório:

Ex: cd /opt/odoo/custom-addons/soulinux


sudo git clone https://github.com/marceloengecom/br_coa_soulinux --branch 15.0


#### Ajuste as permissões dos arquivos e pastas:

Ex: sudo chown -R odoo:odoo /opt/odoo/custom-addons/*


#### No arquivo de configuração /etc/odoo-server.conf, adicione o caminho do novo módulo  na linha "addons_path":

Ex: addons_path = /opt/odoo/custom-addons/soulinux



#### Reinicie o Odoo:

Ex: systemctl restart odoo


#### No Odoo, na interface de instalação de aplicativos, atualize os aplicativos e faça a pesquisa por "br_coa_soulinux"
