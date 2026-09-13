# Exantrix marketplace et Shopify

Relier une boutique Shopify à la marketplace française [Exantrix](https://exantrix.com) sans application à installer : une app personnalisée Shopify, et Exantrix s'abonne aux webhooks de la boutique (produits, stock).

**Guide complet** : https://exantrix.com/extensions/shopify
**Espace vendeur** : https://exantrix.com/a2/vendeur

## Configuration

1. Shopify › Paramètres › Applications et canaux de vente › Développer des applications › Créer une application.
2. Accès API Admin : `read_products`, `read_inventory`. Installer l'app, copier le jeton d'accès et la clé secrète.
3. Espace vendeur Exantrix, section « Votre boutique en ligne » : plateforme Shopify, adresse `monshop.myshopify.com`, jeton, clé secrète, catégorie. Enregistrer : Exantrix crée les webhooks `products/create`, `products/update`, `inventory_levels/update` vers `https://exantrix.com/api/v1/shopify/webhook`.
4. « Importer ma boutique maintenant ». Les nouveaux produits sont validés par Exantrix avant mise en ligne.

## Commandes

Shopify n'accepte pas de commandes externes par ce canal. Chaque commande payée sur Exantrix est envoyée par email et, si une URL est renseignée, par webhook JSON signé HMAC-SHA256 avec le jeton API (`X-Exantrix-Signature: sha256=<hmac>`). Exemple de payload : `exemple-webhook-commande.json` ; vérification de signature : `verifier_signature.py`.

Licence MIT.
