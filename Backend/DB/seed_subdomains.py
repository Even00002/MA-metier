"""
Nom du fichier : seed_subdomains.py
Auteur : Joel Cunha Faria
Date de création : 22.01.2026
Date de modification : 22.01.2026
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from db_schema import engine
from Backend.Class.Class_SubDomain import SubDomain
from Backend.Class.Class_Domain import Domain

def add_subdomain(domain_name: str, sub_name: str, information: str):
    with Session(engine) as session:

        # Récupérer le Domain
        domain = session.execute(
            select(Domain).where(Domain.name == domain_name)
        ).scalar_one_or_none()

        if not domain:
            print(f"Domain introuvable : {domain_name}")
            return

        # Vérifier si le SubDomain existe déjà pour ce Domain
        exists = session.execute(
            select(SubDomain)
            .where(
                SubDomain.name == sub_name,
                SubDomain.domain == domain
            )
        ).scalar_one_or_none()

        if exists:
            print(f"Déjà présent : {sub_name} ({domain_name})")
            return

        # Création ORM (relation directe)
        subdomain = SubDomain(
            name=sub_name,
            information=information,
            domain=domain
        )

        session.add(subdomain)
        session.commit()

        print(f"Ajouté : {sub_name} → {domain_name}")

if __name__ == "__main__":
    # ---- Programmation ----
    add_subdomain(
        "Programmation",
        "Python",
        "Python est un langage de programmation simple, lisible et puissant, très utilisé dans l’enseignement et le monde professionnel. Il est idéal pour débuter grâce à sa syntaxe claire.\n\n"
        "Il permet de créer des scripts, des applications, des programmes d’automatisation, ainsi que des projets en analyse de données et en intelligence artificielle.\n\n"
        "Concepts clés : variables, conditions, boucles, fonctions, listes, dictionnaires et programmation orientée objet.\n\n"
        "Python est un langage interprété, sensible à l’indentation et largement utilisé dans les projets scolaires et professionnels."
    )

    add_subdomain(
        "Programmation",
        "C#",
        "C# est un langage de programmation moderne développé par Microsoft, principalement utilisé avec la plateforme .NET. Il est largement employé pour créer des applications Windows, web et des jeux vidéo.\n\n"
        "C# est un langage orienté objet, fortement typé et structuré, ce qui favorise un code clair, robuste et maintenable.\n\n"
        "Concepts clés : variables, conditions, boucles, classes, objets, héritage, interfaces et gestion des exceptions.\n\n"
        "Au CPNV, C# est souvent utilisé pour apprendre la programmation orientée objet et développer des applications concrètes."
    )

    add_subdomain(
        "Programmation",
        "JavaScript",
        "JavaScript est un langage de programmation principalement utilisé pour le développement web. Il permet de rendre les pages interactives et dynamiques directement dans le navigateur.\n\n"
        "Il est utilisé pour manipuler le contenu HTML et CSS, gérer des événements et communiquer avec des serveurs.\n\n"
        "Concepts clés : variables, conditions, boucles, fonctions, événements, manipulation du DOM et objets.\n\n"
        "JavaScript peut être utilisé côté client (navigateur) et côté serveur grâce à des environnements comme Node.js."
    )

    add_subdomain(
        "Programmation",
        "C++",
        "C++ est un langage de programmation performant, utilisé pour le développement de logiciels nécessitant une gestion fine des ressources. Il est souvent employé pour les systèmes, les jeux vidéo et les applications nécessitant de hautes performances.\n\n"
        "C++ est un langage compilé qui permet un contrôle précis de la mémoire, ce qui le rend puissant mais plus complexe que d’autres langages.\n\n"
        "Concepts clés : variables, conditions, boucles, fonctions, pointeurs, gestion de la mémoire et programmation orientée objet.\n\n"
        "Au CPNV, C++ permet de comprendre le fonctionnement bas niveau des programmes et les principes avancés de la programmation."
    )

    add_subdomain(
        "Programmation",
        "Java",
        "Java est un langage de programmation orienté objet, largement utilisé pour le développement d’applications professionnelles. Il repose sur le principe « écrire une fois, exécuter partout » grâce à la machine virtuelle Java (JVM).\n\n"
        "Java est un langage compilé puis interprété par la JVM, ce qui le rend portable et sécurisé.\n\n"
        "Concepts clés : classes, objets, héritage, interfaces, gestion des exceptions et collections.\n\n"
        "Java est utilisé pour le développement d’applications desktop, web, mobiles (Android) et de systèmes d’entreprise."
    )

    # ---- Web ----
    add_subdomain(
        "Web",
        "HTML",
        "HTML (HyperText Markup Language) est le langage de base du web. Il permet de structurer le contenu d’une page web en définissant les titres, paragraphes, images, liens et autres éléments.\n\n"
        "HTML n’est pas un langage de programmation mais un langage de balisage. Il est interprété par le navigateur.\n\n"
        "Concepts clés : balises, attributs, structure de page, liens, images, formulaires et sémantique.\n\n"
        "HTML est utilisé conjointement avec CSS pour le style et JavaScript pour l’interactivité."
    )

    add_subdomain(
        "Web",
        "CSS",
        "CSS (Cascading Style Sheets) est le langage utilisé pour définir l’apparence et la mise en forme des pages web. Il permet de contrôler les couleurs, polices, tailles, espacements et la disposition des éléments.\n\n"
        "CSS fonctionne en complément du HTML et s’applique aux éléments via des sélecteurs.\n\n"
        "Concepts clés : sélecteurs, propriétés, box model, flexbox, grid et responsive design.\n\n"
        "CSS permet de créer des interfaces modernes, lisibles et adaptées aux différents écrans."
    )

    add_subdomain(
        "Web",
        "JavaScript",
        "JavaScript est le langage qui rend les pages web interactives et dynamiques. "
        "Il permet de modifier le contenu HTML et CSS en temps réel, de réagir aux actions des utilisateurs et de communiquer avec des serveurs via des API.\n\n"
        "Concepts clés : DOM (Document Object Model), événements, fonctions, promesses, fetch/AJAX, ES6+, manipulation des éléments et animations.\n\n"
        "JavaScript côté client transforme une page statique en une interface réactive et moderne, indispensable pour le développement web interactif."
    )

    # ---- Base de données ----
    add_subdomain(
        "Base de données",
        "MCD",
        "Le MCD (Modèle Conceptuel de Données) est une représentation abstraite des données d’un système et de leurs relations. "
        "Il sert à organiser et structurer les informations avant de créer une base de données.\n\n"
        "Concepts clés : entités, attributs, relations, cardinalités, identifiants et contraintes.\n\n"
        "Le MCD permet de concevoir une base de données cohérente et adaptée aux besoins du projet."
    )

    add_subdomain(
        "Base de données",
        "MLD",
        "Le MLD (Modèle Logique de Données) est la traduction du MCD en un modèle exploitable par un Système de Gestion de Base de Données (SGBD). "
        "Il précise les tables, les colonnes, les clés primaires et étrangères, ainsi que les relations entre les tables.\n\n"
        "Concepts clés : tables, attributs, clés primaires/étrangères, relations, normalisation et contraintes d’intégrité.\n\n"
        "Le MLD permet de préparer efficacement la création d’une base de données relationnelle prête à l’implémentation."
    )

    add_subdomain(
        "Base de données",
        "SQL",
        "SQL (Structured Query Language) est le langage utilisé pour interagir avec les bases de données relationnelles. "
        "Il permet de créer, lire, mettre à jour et supprimer des données (opérations CRUD) ainsi que de gérer la structure des tables.\n\n"
        "Concepts clés : SELECT, INSERT, UPDATE, DELETE, JOIN, contraintes, clés primaires/étrangères, index et transactions.\n\n"
        "SQL est essentiel pour manipuler et interroger efficacement les données dans tout projet utilisant une base relationnelle."
    )

    # ---- Systèmes & Réseaux ----
    add_subdomain(
        "Systèmes & Réseaux",
        "Paramètres",
        "Les paramètres d’un système ou d’un réseau désignent les configurations qui définissent le fonctionnement des équipements et logiciels. "
        "Ils permettent de contrôler l’accès, la sécurité, la performance et le comportement des systèmes.\n\n"
        "Concepts clés : adresses IP, masque de sous-réseau, passerelle, DNS, protocoles, droits d’accès et configurations réseau.\n\n"
        "Bien gérer les paramètres est essentiel pour assurer la stabilité, la sécurité et l’efficacité d’un réseau ou d’un système."
    )

    add_subdomain(
        "Systèmes & Réseaux",
        "Invite de commande",
        "L’invite de commande est une interface textuelle qui permet d’interagir directement avec le système d’exploitation en tapant des commandes. "
        "Elle est utilisée pour exécuter des programmes, gérer des fichiers, configurer des paramètres ou diagnostiquer des problèmes.\n\n"
        "Concepts clés : commandes de navigation (cd, dir/ls), gestion de fichiers (copy, move, rm), gestion réseau (ping, ipconfig/ifconfig), scripts et automatisation.\n\n"
        "L’invite de commande est un outil puissant pour administrer un système ou un réseau de manière rapide et précise."
    )

    add_subdomain(
        "Systèmes & Réseaux",
        "Réseau",
        "Un réseau est un ensemble d’équipements connectés entre eux pour échanger des données et partager des ressources. "
        "Il peut être local (LAN), étendu (WAN) ou sans fil (Wi-Fi), et repose sur des protocoles pour assurer la communication.\n\n"
        "Concepts clés : IP, sous-réseau, routeurs, switches, protocoles TCP/IP, DNS, DHCP et sécurité réseau.\n\n"
        "Comprendre les réseaux est essentiel pour configurer, sécuriser et optimiser la communication entre les systèmes."
    )

    add_subdomain(
        "Systèmes & Réseaux",
        "Gestion d'ordinateur",
        "La gestion d'ordinateur regroupe l’ensemble des actions permettant d’administrer et maintenir un système informatique. "
        "Elle inclut la gestion des fichiers, des utilisateurs, des logiciels, des périphériques et des performances du système.\n\n"
        "Concepts clés : gestion des comptes utilisateurs, permissions, gestion des fichiers et dossiers, installation de logiciels, mises à jour, sauvegardes et maintenance.\n\n"
        "Une bonne gestion d’ordinateur assure sécurité, efficacité et stabilité du système pour l’utilisateur comme pour le réseau."
    )

    # ---- Outils & Méthodes ----
    add_subdomain(
        "Outils & Méthodes",
        "Lien du CPNV",
        "Le Lien du CPNV est la plateforme en ligne officielle du Centre Professionnel du Nord Vaudois. "
        "Elle permet aux étudiants et enseignants d’accéder aux informations administratives, aux ressources pédagogiques et aux communications internes.\n\n"
        "Concepts clés : accès aux cours, calendrier, documents, notes, messagerie interne et informations administratives.\n\n"
        "Accède au Lien du CPNV ici : https://www.cpnv.ch/app/uploads/CPNV-memento.pdf\n\n"
        "Utiliser le Lien du CPNV facilite le suivi des cours, la gestion des travaux et la communication avec le personnel de l’école."
    )

    add_subdomain(
        "Outils & Méthodes",
        "Lien de l'intranet",
        "Le Lien de l’intranet est la plateforme interne d’une organisation qui centralise les informations, documents et outils destinés aux employés ou étudiants. "
        "Il permet de consulter les actualités, accéder aux ressources partagées et collaborer avec les différents services.\n\n"
        "Concepts clés : accès sécurisé, documents partagés, messagerie interne, annonces, calendrier et outils collaboratifs.\n\n"
        "Accède à l’intranet du CPNV ici : https://intranet.cpnv.ch/\n\n"
        "Utiliser l’intranet facilite la communication interne, l’organisation du travail et l’accès aux ressources essentielles."
    )

    # ---- Aide scolaire IT ----
    add_subdomain(
        "Aide scolaire IT",
        "Lien du Memento",
        "Le Lien du Memento donne accès à un guide ou résumé des notions essentielles en informatique pour les étudiants. "
        "Il permet de réviser rapidement les concepts clés et de retrouver des explications pratiques.\n\n"
        "Concepts clés : synthèses, astuces, rappels des cours, commandes et bonnes pratiques.\n\n"
        "Accède au Mémento du CPNV ici : [Mémento PDF](https://www.cpnv.ch/app/uploads/CPNV-memento.pdf)\n\n"
        "Le Memento est un outil pratique pour soutenir l’apprentissage et la révision des notions IT."
    )

    add_subdomain(
        "Aide scolaire IT",
        "Lien pour du Soutien",
        "Le Lien pour du Soutien fournit des ressources et contacts pour aider les étudiants rencontrant des difficultés en informatique. "
        "Il peut inclure tutoriels, exercices guidés, forums et assistance personnalisée.\n\n"
        "Concepts clés : tutoriels, exercices, FAQ, accompagnement individuel et ressources complémentaires.\n\n"
        "Ressources et support informatique : [Support IT](https://www.cpnv.ch/vivre-au-cpnv/informatique/)\n\n"
        "Ce lien facilite l’accès à l’aide nécessaire pour progresser efficacement en IT."
    )

    add_subdomain(
        "Aide scolaire IT",
        "Lien pour le Règlement",
        "Le Lien pour le Règlement donne accès aux règles et directives officielles de l’école ou du département IT. "
        "Il précise les droits, obligations et bonnes pratiques attendues des étudiants.\n\n"
        "Concepts clés : règles de conduite, évaluation, devoirs, sanctions et procédures administratives.\n\n"
        "Consulte les règlements officiels : [Règlements CPNV](https://www.cpnv.ch/vivre-au-cpnv/reglements/)\n\n"
        "Consulter le règlement permet de respecter les normes et de suivre correctement le cadre scolaire."
    )