# Exantrix marketplace et Shopify

Connexion pour [Shopify](https://www.shopify.com) (code source et outils officiels : [github.com/Shopify](https://github.com/Shopify), API Admin : [shopify.dev](https://shopify.dev/docs/api/admin-rest)).

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

## Plateformes : sites et sources

| Plateforme | Site officiel | Code source | Documentation développeur |
|---|---|---|---|
| Shopify | https://www.shopify.com | https://github.com/Shopify | https://shopify.dev/docs/api/admin-rest |
| Shopify webhooks | https://shopify.dev/docs/apps/build/webhooks | — | — |

## Les extensions Exantrix

- [WordPress / WooCommerce](https://github.com/tony-dev-web/exantrix-marketplace-wordpress)
- [PrestaShop](https://github.com/tony-dev-web/exantrix-marketplace-prestashop)
- [Magento 2](https://github.com/tony-dev-web/exantrix-marketplace-magento)
- [Drupal Commerce](https://github.com/tony-dev-web/exantrix-marketplace-drupal)
- [CSV / Excel, Odoo, Dolibarr (sans installation)](https://github.com/tony-dev-web/exantrix-marketplace-connecteurs)
- [API : collection Postman et OpenAPI](https://github.com/tony-dev-web/exantrix-api)
- Site et API : [exantrix.com](https://github.com/tony-dev-web/exantrix.com) (source de la marketplace, Django) — https://exantrix.com/extensions/
