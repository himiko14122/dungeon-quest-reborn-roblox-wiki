#!/usr/bin/env python3
"""Rewrite metadata.title/description for 292 MDX articles across 4 languages."""
import re
from pathlib import Path

CONTENT_DIR = Path("/Users/jinwei/Desktop/code/dungeon-quest-reborn-roblox/content")

EN_TITLES = {
    "boss-guide": "Dungeon Quest Reborn: Full Boss Strategy & Tactics Guide",
    "boss-comparison": "Dungeon Quest Reborn: Boss Rewards & Drop Rates Ranked",
    "boss-enrage-timer": "Dungeon Quest Reborn: Boss Enrage Timer Mechanics Guide",
    "boss-health-guide": "Dungeon Quest Reborn: All Boss HP Values & Weaknesses",
    "boss-rush-guide": "Dungeon Quest Reborn: Boss Rush Mode Complete Strategy",
    "easiest-boss": "Dungeon Quest Reborn: Easiest Boss & Winning Strategy",
    "how-to-beat-bosses-solo": "Dungeon Quest Reborn: Solo Every Boss Strategy Guide",
    "how-to-beat-winter-outpost-boss": "Dungeon Quest Reborn: Winter Outpost Boss Solo Guide",
    "class-exclusive-gear": "Dungeon Quest Reborn: Class-Exclusive Gear & Items Guide",
    "class-guide": "Dungeon Quest Reborn: Warrior vs Mage Full Class Guide",
    "class-specific-dungeons": "Dungeon Quest Reborn: Class-Specific Dungeons Guide",
    "class-tier-list": "Dungeon Quest Reborn: Class Tier List & Best Rankings",
    "hybrid-build": "Dungeon Quest Reborn: Best Hybrid Build Guide & Tips",
    "warrior-ability-rotation": "Dungeon Quest Reborn: Warrior Ability Combo Rotations",
    "warrior-stat-priority": "Dungeon Quest Reborn: Warrior Stat Priority Explained",
    "warrior-tips": "Dungeon Quest Reborn: Warrior Tips & Advanced Tactics Guide",
    "desert-temple-guide": "Dungeon Quest Reborn: Desert Temple Full Walkthrough",
    "dungeon-armor-drops": "Dungeon Quest Reborn: Dungeon Armor Drops Guide 2026",
    "dungeon-difficulty-levels": "Dungeon Quest Reborn: All Dungeon Difficulty Tiers Explained",
    "dungeon-layout-guide": "Dungeon Quest Reborn: Every Dungeon Layout & Secrets",
    "dungeon-ranking": "Dungeon Quest Reborn: All Dungeons Ranked from Best",
    "dungeon-tier-list": "Dungeon Quest Reborn: Dungeon Tier List & Rankings",
    "pirate-island-boss": "Dungeon Quest Reborn: Pirate Island Boss Guide 2026",
    "winter-outpost-walkthrough": "Dungeon Quest Reborn: Winter Outpost Complete Guide",
    "best-equipment-for-warrior": "Dungeon Quest Reborn: Best Warrior Equipment Rankings",
    "best-equipment": "Dungeon Quest Reborn: Best Equipment in the Game Ranked",
    "equipment-glitches": "Dungeon Quest Reborn: Equipment Glitches & How to Fix",
    "equipment-level-requirements": "Dungeon Quest Reborn: Every Equipment Level Requirement",
    "equipment-meta": "Dungeon Quest Reborn: Equipment Meta Breakdown Guide",
    "equipment-stat-priority": "Dungeon Quest Reborn: Equipment Stat Priority Guide",
    "event-equipment": "Dungeon Quest Reborn: Event Equipment Guide & Rewards",
    "physical-power-gear": "Dungeon Quest Reborn: Physical Power Gear Guide 2026",
    "beginner-guide": "Dungeon Quest Reborn: Complete Beginner Guide & Tips 2026",
    "best-farming-spots": "Dungeon Quest Reborn: Best Farming Spots & XP Routes",
    "drop-rate-guide": "Dungeon Quest Reborn: Drop Rate Guide & Farming Tips",
    "how-to-clear-dungeons-fast": "Dungeon Quest Reborn: Fast Dungeon Clear Routes Guide",
    "how-to-compare-equipment": "Dungeon Quest Reborn: How to Compare Equipment Stats",
    "how-to-level-fast": "Dungeon Quest Reborn: How to Level Up Fast in Game",
    "how-to-unlock-winter-outpost": "Dungeon Quest Reborn: How to Unlock Winter Outpost",
    "season-guide": "Dungeon Quest Reborn: Season Guide & Full Roadmap 2026",
    "speed-run-guide": "Dungeon Quest Reborn: Speed Run Guide & Best Routes 2026",
    "when-to-move-to-next-dungeon": "Dungeon Quest Reborn: When to Move to Next Dungeon",
    "best-spells": "Dungeon Quest Reborn: Best Spells Tier List & Rankings",
    "how-to-get-rare-spells": "Dungeon Quest Reborn: How to Get Rare Spells Guide",
    "spell-animation-guide": "Dungeon Quest Reborn: Spell Animation Cancel Guide",
    "spell-area-of-effect": "Dungeon Quest Reborn: Spell AoE Range Explained Guide",
    "spell-comparison": "Dungeon Quest Reborn: Spell Comparison & DPS Rankings",
    "spell-drop-locations": "Dungeon Quest Reborn: All Spell Drop Locations Guide",
    "spell-level-requirements": "Dungeon Quest Reborn: All Spell Level Requirements",
    "spell-meta": "Dungeon Quest Reborn: Current Spell Meta & Best Picks Guide",
    "best-overall-tier-list": "Dungeon Quest Reborn: Best Overall Tier List Rankings",
    "c-tier-weapons": "Dungeon Quest Reborn: C-Tier Weapons List & Full Stats",
    "early-game-tier-list": "Dungeon Quest Reborn: Early Game Tier List Rankings",
    "tier-list-explanation": "Dungeon Quest Reborn: How Tier List Rankings Explained",
    "tier-list-history": "Dungeon Quest Reborn: Tier List History & Patch Changes",
    "tier-list-rankings": "Dungeon Quest Reborn: Full Tier List Rankings Guide",
    "tier-list-update": "Dungeon Quest Reborn: Latest Tier List Update & Changes",
    "tier-list": "Dungeon Quest Reborn: Complete Tier List & All Rankings 2026",
    "community-update": "Dungeon Quest Reborn: Community Update & News 2026",
    "major-update": "Dungeon Quest Reborn: Major Update Full Breakdown Guide",
    "new-dungeon": "Dungeon Quest Reborn: New Dungeon Reveal & Complete Guide",
    "patch-notes": "Dungeon Quest Reborn: Latest Patch Notes & Balance Changes",
    "quality-of-life-update": "Dungeon Quest Reborn: Quality of Life Update Guide",
    "roadmap": "Dungeon Quest Reborn: Full Roadmap & Future Content Plans",
    "seasonal-event": "Dungeon Quest Reborn: Seasonal Event Guide & Rewards",
    "update-review": "Dungeon Quest Reborn: Update Review & Meta Analysis 2026",
    "best-dagger": "Dungeon Quest Reborn: Best Daggers Ranked by DPS Guide",
    "best-weapon-for-farming": "Dungeon Quest Reborn: Best Weapon for Farming Guide",
    "best-weapons": "Dungeon Quest Reborn: Best Weapons Tier List & Rankings",
    "legendary-weapons-list": "Dungeon Quest Reborn: All Legendary Weapons List Guide",
    "pirate-island-weapons": "Dungeon Quest Reborn: Pirate Island Weapons Guide 2026",
    "unobtainable-weapons": "Dungeon Quest Reborn: Unobtainable Weapons List Guide",
    "weapon-market": "Dungeon Quest Reborn: Weapon Market & Trading Guide",
    "weapon-upgrade-cost": "Dungeon Quest Reborn: Weapon Upgrade Costs Full Guide",
}

EN_DESCS = {
    "boss-guide": "Master every boss in Dungeon Quest Reborn with detailed strategies, attack patterns, and solo tactics for Sand Giant and all dungeon encounters.",
    "boss-comparison": "Compare all bosses by reward value and drop rates in Dungeon Quest Reborn. Discover which bosses are worth farming and which to skip for efficiency.",
    "boss-enrage-timer": "Learn the exact enrage timers for every boss in Dungeon Quest Reborn. Understand the mechanics and how to counter them before time runs out.",
    "boss-health-guide": "All boss HP values and weaknesses revealed. Discover which weapons and spells deal the most damage to each boss and exploit elemental weaknesses.",
    "boss-rush-guide": "Conquer Boss Rush mode with proven strategies for every wave in Dungeon Quest Reborn. Learn the best class, equipment, and spell loadout to win.",
    "easiest-boss": "Discover the easiest boss to beat in Dungeon Quest Reborn. This guide covers the best loadout, positioning strategy, and farming route for wins.",
    "how-to-beat-bosses-solo": "Solo every boss in Dungeon Quest Reborn with confidence. Learn the exact strategy, equipment, and stat requirements to defeat every boss alone.",
    "how-to-beat-winter-outpost-boss": "Defeat the Winter Outpost boss in Dungeon Quest Reborn with this complete strategy guide. Learn attack patterns, phase mechanics, and the best solo tactics.",
    "class-exclusive-gear": "Discover all class-exclusive gear for Warrior and Mage in Dungeon Quest Reborn. Learn where to find each piece and which items are worth farming.",
    "class-guide": "Choose the right class with our Warrior vs Mage comparison. Learn stat differences, ability mechanics, equipment synergy, and optimal playstyles.",
    "class-specific-dungeons": "Unlock class-specific dungeons in Dungeon Quest Reborn. Learn the entry requirements, exclusive rewards, and best strategies for each encounter.",
    "class-tier-list": "The definitive class tier list ranking Warrior and Mage builds in Dungeon Quest Reborn. See which class dominates the PvE and endgame content.",
    "hybrid-build": "Build the ultimate hybrid character in Dungeon Quest Reborn. Learn to combine Warrior and Mage abilities, optimize stats, and dominate with creative builds.",
    "warrior-ability-rotation": "Master the optimal Warrior ability rotation and combo order in Dungeon Quest Reborn. Learn timing windows and ability synergies for max DPS.",
    "warrior-stat-priority": "Maximize your Warrior damage with the correct stat priority in Dungeon Quest Reborn. Learn which stats matter most at every level of character progression.",
    "warrior-tips": "Improve your Warrior gameplay with advanced tips and tricks in Dungeon Quest Reborn. Learn positioning, ability cancels, and PvP combat techniques.",
    "desert-temple-guide": "Complete walkthrough of Desert Temple in Dungeon Quest Reborn. Learn every enemy type, room layout, boss mechanics, and optimal loot routes.",
    "dungeon-armor-drops": "Find the best armor drops from every dungeon in Dungeon Quest Reborn. Learn drop rates, stat ranges, and which dungeons to farm for each piece.",
    "dungeon-difficulty-levels": "Understand all dungeon difficulty tiers from Normal to Nightmare in Dungeon Quest Reborn. Learn stat requirements, reward scaling, and strategies.",
    "dungeon-layout-guide": "Navigate every dungeon with our complete layout guide. Learn room connections, hidden paths, trap locations, and the fastest routes to each boss.",
    "dungeon-ranking": "All dungeons ranked from best to worst in Dungeon Quest Reborn. Compare rewards, difficulty, clear times, and loot quality to prioritize your farming.",
    "dungeon-tier-list": "The complete dungeon tier list for Dungeon Quest Reborn. Every dungeon ranked by reward value, difficulty, and efficiency for your farming routes.",
    "pirate-island-boss": "Defeat the Pirate Island boss with expert strategies. Learn phase transitions, attack patterns, and the best solo and group tactics for this fight.",
    "winter-outpost-walkthrough": "Full walkthrough of Winter Outpost in Dungeon Quest Reborn. Discover every enemy, trap, puzzle solution, boss mechanics, and hidden rewards.",
    "best-equipment-for-warrior": "Find the best Warrior equipment for every level in Dungeon Quest Reborn. Learn which weapons, armor, and accessories maximize damage and survivability.",
    "best-equipment": "The ultimate best equipment guide with comparisons of top-tier weapons, armor, and accessories. Get stat breakdowns and recommendations for each class.",
    "equipment-glitches": "Discover known equipment glitches in Dungeon Quest Reborn and how to fix them. Learn which bugs still exist and what to do if you encounter one.",
    "equipment-level-requirements": "All equipment level requirements listed for Dungeon Quest Reborn. Plan your progression and know exactly when you can equip each weapon and armor piece.",
    "equipment-meta": "Analyze the current equipment meta in Dungeon Quest Reborn. Learn which items dominate PvE and PvP and what to prioritize for your progression.",
    "equipment-stat-priority": "Optimize your equipment stat priority in Dungeon Quest Reborn. Learn which stats scale best for Warrior and Mage and how to roll perfect gear.",
    "event-equipment": "Complete guide to event equipment in Dungeon Quest Reborn. Learn how to obtain limited-time gear, complete challenges, and maximize your rewards.",
    "physical-power-gear": "Maximize your physical power with the best gear in Dungeon Quest Reborn. Learn which items boost physical damage and how to stack stats for peak performance.",
    "beginner-guide": "Start your Dungeon Quest Reborn journey with our beginner guide. Learn core mechanics, best early-game choices, leveling tips, and common mistakes to avoid.",
    "best-farming-spots": "Discover the best farming spots for XP, currency, and rare drops. Learn optimal routes, respawn timers, and efficiency tips for maximum hourly gains.",
    "drop-rate-guide": "All drop rates revealed for weapons, spells, and equipment in Dungeon Quest Reborn. Learn exact percentages and the most efficient farming strategies.",
    "how-to-clear-dungeons-fast": "Speed up your dungeon clears with proven strategies. Learn optimal routes, skip tactics, ability usage, and team coordination tips for faster runs.",
    "how-to-compare-equipment": "Learn how to compare equipment like a pro. Understand stat calculations, DPS formulas, and hidden mechanics that determine which item is truly better.",
    "how-to-level-fast": "Level up fast with the most efficient XP methods. Learn the best dungeons to farm, optimal routes, XP boosts, and time-saving tips for rapid progression.",
    "how-to-unlock-winter-outpost": "Unlock Winter Outpost in Dungeon Quest Reborn with our step-by-step guide. Learn the quest requirements, level recommendations, and what to expect inside.",
    "season-guide": "Complete season guide for Dungeon Quest Reborn. Learn the battle pass rewards, seasonal challenges, limited-time content, and how to maximize progress.",
    "speed-run-guide": "Master speed running in Dungeon Quest Reborn with optimal routes and strategies. Learn the fastest dungeon clear times and leaderboard techniques.",
    "when-to-move-to-next-dungeon": "Know exactly when to move to the next dungeon in Dungeon Quest Reborn. Learn level benchmarks, stat goals, and gear checklists for a smooth progression.",
    "best-spells": "Find the best spells ranked by DPS, utility, and versatility in Dungeon Quest Reborn. This tier list covers every spell from common to legendary.",
    "how-to-get-rare-spells": "Learn how to get rare spells with proven farming methods. Discover drop locations, pull strategies, and the most reliable ways to build your collection.",
    "spell-animation-guide": "Complete spell animation guide for Dungeon Quest Reborn covering cast times, cancel windows, and animation priority. Learn how to cancel spells for max DPS.",
    "spell-area-of-effect": "Maximize your AoE damage with accurate spell area-of-effect data in Dungeon Quest Reborn. Learn exact radii, damage falloff, and positioning.",
    "spell-comparison": "Compare all spells in Dungeon Quest Reborn with detailed DPS calculations. Learn which spells excel at single target versus AoE for your spell loadout.",
    "spell-drop-locations": "Find every spell drop location in Dungeon Quest Reborn. Learn which bosses, dungeons, and events drop each spell along with exact drop rates and tips.",
    "spell-level-requirements": "All spell level requirements listed for every spell in Dungeon Quest Reborn. Plan your build path and know exactly when you can equip each new spell.",
    "spell-meta": "Explore the current spell meta in Dungeon Quest Reborn. Learn which spells dominate PvE, how they synergize with equipment, and what to prioritize.",
    "best-overall-tier-list": "The definitive best overall tier list for Dungeon Quest Reborn ranking every weapon, spell, and class. Updated with the latest meta changes and community data.",
    "c-tier-weapons": "Complete C-tier weapons list with full stats and descriptions. Learn which weapons to avoid, their hidden niche uses, and when they might surprise you.",
    "early-game-tier-list": "The essential early game tier list ranking every starter weapon, spell, and class option. Make the best choices from your very first dungeon run.",
    "tier-list-explanation": "Understand how Dungeon Quest Reborn tier lists work and what each rank means. Learn the criteria used to evaluate weapons, spells, and equipment.",
    "tier-list-history": "Track every change across Dungeon Quest Reborn tier lists over multiple patches. See how weapons and spells have risen or fallen with each game update.",
    "tier-list-rankings": "Full tier list rankings for Dungeon Quest Reborn covering all weapons, spells, and classes. Quickly compare item power levels and make informed gear decisions.",
    "tier-list-update": "The latest tier list update for Dungeon Quest Reborn reflecting the current patch. See all rank changes, new weapon additions, and meta shifts affecting builds.",
    "tier-list": "The complete tier list ranking all weapons, spells, and classes in Dungeon Quest Reborn. Updated regularly with community data and expert analysis.",
    "community-update": "Catch up on the latest community update for Dungeon Quest Reborn. Learn about upcoming features, developer announcements, and community events.",
    "major-update": "Complete breakdown of the latest major update in Dungeon Quest Reborn. Discover new dungeons, weapons, spells, balance changes, and QoL improvements.",
    "new-dungeon": "Explore the newest dungeon added to Dungeon Quest Reborn. Learn the layout, enemies, boss mechanics, exclusive rewards, and how to access it.",
    "patch-notes": "Read the latest patch notes with full balance changes in Dungeon Quest Reborn. Learn what was buffed, what was nerfed, and how the meta shifts.",
    "quality-of-life-update": "Discover all quality-of-life updates in Dungeon Quest Reborn. Learn about new UI features, convenience improvements, bug fixes, and gameplay tweaks.",
    "roadmap": "Explore the full development roadmap for Dungeon Quest Reborn. Learn about planned dungeons, weapons, classes, seasonal events, and future game content.",
    "seasonal-event": "Participate in the current seasonal event in Dungeon Quest Reborn. Learn event challenges, exclusive rewards, time limits, and the best strategy.",
    "update-review": "Honest review of the latest Dungeon Quest Reborn update. We analyze new content, assess balance changes, and rate whether the game has improved.",
    "best-dagger": "Find the best daggers ranked by DPS and utility in Dungeon Quest Reborn. Learn dagger-specific strategies, stat priorities, and which excel at PvE.",
    "best-weapon-for-farming": "Discover the best weapon for farming XP, currency, and rare drops. Learn which weapons offer the best clear speed and efficiency for your goals.",
    "best-weapons": "The complete best weapons ranking with every weapon tier from S to D. Includes stat comparisons, DPS calculations, and class-specific recommendations.",
    "legendary-weapons-list": "Complete list of all legendary weapons with drop locations in Dungeon Quest Reborn. Learn where to farm each legendary and their unique abilities.",
    "pirate-island-weapons": "Discover all Pirate Island weapons in Dungeon Quest Reborn. Learn drop rates, stat ranges, unique abilities, and which weapons are worth farming.",
    "unobtainable-weapons": "List of all unobtainable weapons in Dungeon Quest Reborn. Learn which items have been removed, why they were vaulted, and if they might return.",
    "weapon-market": "Navigate the weapon market in Dungeon Quest Reborn like an expert. Learn trading strategies, price trends, fair values, and how to profit from weapon trades.",
    "weapon-upgrade-cost": "All weapon upgrade costs listed from level 1 to max in Dungeon Quest Reborn. Plan your currency spending with exact costs per weapon rarity tier.",
}


ES_TITLES = {
    "boss-guide": "Dungeon Quest Reborn: Guía Completa de Todos los Jefes",
    "boss-comparison": "Dungeon Quest Reborn: Comparación de Jefes y Drops Guía",
    "boss-enrage-timer": "Dungeon Quest Reborn: Temporizador Enfado de los Jefes",
    "boss-health-guide": "Dungeon Quest Reborn: HP y Debilidades de Cada Jefe",
    "boss-rush-guide": "Dungeon Quest Reborn: Guía Modo Boss Rush Completa",
    "easiest-boss": "Dungeon Quest Reborn: El Jefé Más Fácil y Cómo Ganar",
    "how-to-beat-bosses-solo": "Dungeon Quest Reborn: Vencer Todos los Jefes en Solo",
    "how-to-beat-winter-outpost-boss": "Dungeon Quest Reborn: Guía del Jefe de Winter Outpost",
    "class-exclusive-gear": "Dungeon Quest Reborn: Equipo Exclusivo por Clase Guía",
    "class-guide": "Dungeon Quest Reborn: Guerrero vs Mago Guía Completa",
    "class-specific-dungeons": "Dungeon Quest Reborn: Mazmorras Exclusivas por Clase",
    "class-tier-list": "Dungeon Quest Reborn: Tier List de Clases Completa",
    "hybrid-build": "Dungeon Quest Reborn: Mejor Build Híbrida del Juego",
    "warrior-ability-rotation": "Dungeon Quest Reborn: Rotación de Habilidades Guerrero",
    "warrior-stat-priority": "Dungeon Quest Reborn: Prioridad Stats del Guerrero Guía",
    "warrior-tips": "Dungeon Quest Reborn: Tips Avanzados Guerrero Juego",
    "desert-temple-guide": "Dungeon Quest Reborn: Guía Completa Templo del Desierto",
    "dungeon-armor-drops": "Dungeon Quest Reborn: Drops de Armadura en Mazmorras Guía",
    "dungeon-difficulty-levels": "Dungeon Quest Reborn: Niveles de Dificultad Mazmorras",
    "dungeon-layout-guide": "Dungeon Quest Reborn: Layout de Todas las Mazmorras Guía",
    "dungeon-ranking": "Dungeon Quest Reborn: Ranking de Todas las Mazmorras Guía",
    "dungeon-tier-list": "Dungeon Quest Reborn: Tier List de Mazmorras del Juego",
    "pirate-island-boss": "Dungeon Quest Reborn: Guía del Jefe de la Isla Pirata",
    "winter-outpost-walkthrough": "Dungeon Quest Reborn: Walkthrough de Winter Outpost Guía",
    "best-equipment-for-warrior": "Dungeon Quest Reborn: Mejor del Guerrero Equipo Guía",
    "best-equipment": "Dungeon Quest Reborn: Mejor Equipo del Juego Ranked",
    "equipment-glitches": "Dungeon Quest Reborn: Glitches de Equipo y Fixes Guía",
    "equipment-level-requirements": "Dungeon Quest Reborn: Niveles Requeridos Equipo Guía",
    "equipment-meta": "Dungeon Quest Reborn: Meta Actual del Equipo del Juego",
    "equipment-stat-priority": "Dungeon Quest Reborn: Prioridad Stats Equipo Guerrero",
    "event-equipment": "Dungeon Quest Reborn: Equipo de Eventos y Recompensas Guía",
    "physical-power-gear": "Dungeon Quest Reborn: Equipo de Poder Físico Completo",
    "beginner-guide": "Dungeon Quest Reborn: Guía para Principiantes Completa",
    "best-farming-spots": "Dungeon Quest Reborn: Mejores Spots de Farmeo y XP Guía",
    "drop-rate-guide": "Dungeon Quest Reborn: Guía de Drop Rates del Juego",
    "how-to-clear-dungeons-fast": "Dungeon Quest Reborn: Limpiar Mazmorras Rápido Guía",
    "how-to-compare-equipment": "Dungeon Quest Reborn: Cómo Comparar Equipo Como Pro",
    "how-to-level-fast": "Dungeon Quest Reborn: Subir Nivel Rápido del Juego Guía",
    "how-to-unlock-winter-outpost": "Dungeon Quest Reborn: Desbloquear Winter Outpost Guía",
    "season-guide": "Dungeon Quest Reborn: Guía Temporada Detallada del Jogo",
    "speed-run-guide": "Dungeon Quest Reborn: Guía Speed Run y Récords del Jogo",
    "when-to-move-to-next-dungeon": "Dungeon Quest Reborn: Cuándo Cambiar de Mazmorra Guía",
    "best-spells": "Dungeon Quest Reborn: Mejores Hechizos Tier del Jogo",
    "how-to-get-rare-spells": "Dungeon Quest Reborn: Conseguir Hechizos Raros Guía",
    "spell-animation-guide": "Dungeon Quest Reborn: Animaciones de Hechizos del Jogo",
    "spell-area-of-effect": "Dungeon Quest Reborn: Área de Efecto de Hechizos Guía",
    "spell-comparison": "Dungeon Quest Reborn: Comparación de Hechizos y DPS Guía",
    "spell-drop-locations": "Dungeon Quest Reborn: Drops de Hechizos y Ubicaciones",
    "spell-level-requirements": "Dungeon Quest Reborn: Niveles Requeridos de Hechizos",
    "spell-meta": "Dungeon Quest Reborn: Meta Actual de Hechizos del Jogo",
    "best-overall-tier-list": "Dungeon Quest Reborn: Mejor Tier List General del Jogo",
    "c-tier-weapons": "Dungeon Quest Reborn: Armas C-Tier Lista y Stats Guerrero",
    "early-game-tier-list": "Dungeon Quest Reborn: Tier List de Inicio del Jogo",
    "tier-list-explanation": "Dungeon Quest Reborn: Cómo Funciona la Tier List Guía",
    "tier-list-history": "Dungeon Quest Reborn: Historial de Cambios en Tier List",
    "tier-list-rankings": "Dungeon Quest Reborn: Rankings Completos de Tier List",
    "tier-list-update": "Dungeon Quest Reborn: Última Actualización Tier List Jogo",
    "tier-list": "Dungeon Quest Reborn: Tier List Completa y Rankings Jogo",
    "community-update": "Dungeon Quest Reborn: Update de la Comunidad del Jogo",
    "major-update": "Dungeon Quest Reborn: Gran Actualización del Jogo Detalles",
    "new-dungeon": "Dungeon Quest Reborn: Nueva Mazmorra Guía Completa Jogo",
    "patch-notes": "Dungeon Quest Reborn: Notas del Parche y Cambios Guía",
    "quality-of-life-update": "Dungeon Quest Reborn: Mejoras QoL del Jogo Detalles",
    "roadmap": "Dungeon Quest Reborn: Roadmap del Jogo Completo y Detallado",
    "seasonal-event": "Dungeon Quest Reborn: Evento de Temporada del Jogo",
    "update-review": "Dungeon Quest Reborn: Review de la Actualización Guía",
    "best-dagger": "Dungeon Quest Reborn: Mejores Dagas Ranking del Jogo",
    "best-weapon-for-farming": "Dungeon Quest Reborn: Mejor Arma para Farming Guía",
    "best-weapons": "Dungeon Quest Reborn: Mejores Armas Tier del Jogo",
    "legendary-weapons-list": "Dungeon Quest Reborn: Lista de Armas Legendarias Guía",
    "pirate-island-weapons": "Dungeon Quest Reborn: Armas de la Isla Pirata del Jogo",
    "unobtainable-weapons": "Dungeon Quest Reborn: Armas Inobtenibles Lista Completa",
    "weapon-market": "Dungeon Quest Reborn: Mercado de Armas Trading Guía",
    "weapon-upgrade-cost": "Dungeon Quest Reborn: Coste de Upgrade de Armas Guía",
}

ES_TITLES = {k: v.replace("Jogo", "Juego") for k, v in ES_TITLES.items()}

# Validate
err = 0
for slug, t in ES_TITLES.items():
    if len(t) < 50 or len(t) > 60:
        print(f"ES FAIL {len(t)}c: {slug}")
        err += 1
if err == 0:
    print(f"ES titles OK ({len(ES_TITLES)} entries)")


FR_TITLES = {
    "boss-guide": "Dungeon Quest Reborn : Guide Complet de Tous les Boss du Jeu",
    "boss-comparison": "Dungeon Quest Reborn : Comparaison des Boss et Drops Guide",
    "boss-enrage-timer": "Dungeon Quest Reborn : Timer Enrage des Boss du Jeu Guide",
    "boss-health-guide": "Dungeon Quest Reborn : PV et Faiblesses de Tous les Boss",
    "boss-rush-guide": "Dungeon Quest Reborn : Guide Complet Mode Boss Rush Jeu",
    "easiest-boss": "Dungeon Quest Reborn : Boss le Plus Facile et Comment Gagner",
    "how-to-beat-bosses-solo": "Dungeon Quest Reborn : Vaincre les Boss du Jeu en Solo",
    "how-to-beat-winter-outpost-boss": "Dungeon Quest Reborn : Guide Complet Boss Winter Outpost",
    "class-exclusive-gear": "Dungeon Quest Reborn : Équipement Exclusif par Classe Guide",
    "class-guide": "Dungeon Quest Reborn : Guerrier vs Mage Guide Complet du Jeu",
    "class-specific-dungeons": "Dungeon Quest Reborn : Donjons Exclusifs de Chaque Classe",
    "class-tier-list": "Dungeon Quest Reborn : Tier List des Classes du Jeu Guide",
    "hybrid-build": "Dungeon Quest Reborn : Meilleure Build Hybride du Jeu Guide",
    "warrior-ability-rotation": "Dungeon Quest Reborn : Rotation des Compétences Guerrier",
    "warrior-stat-priority": "Dungeon Quest Reborn : Priorité des Stats du Guerrier Guide",
    "warrior-tips": "Dungeon Quest Reborn : Tips Avancés pour Guerrier du Jeu",
    "desert-temple-guide": "Dungeon Quest Reborn : Guide Temple Désert Complet du Jeu",
    "dungeon-armor-drops": "Dungeon Quest Reborn : Drops Armure Donjons Guide Complet",
    "dungeon-difficulty-levels": "Dungeon Quest Reborn : Niveaux Difficulté des Donjons",
    "dungeon-layout-guide": "Dungeon Quest Reborn : Layout Complet de Tous les Donjons",
    "dungeon-ranking": "Dungeon Quest Reborn : Classement de Tous les Donjons Guide",
    "dungeon-tier-list": "Dungeon Quest Reborn : Tier List Complète des Donjons Jeu",
    "pirate-island-boss": "Dungeon Quest Reborn : Guide du Boss Île des Pirates Jeu",
    "winter-outpost-walkthrough": "Dungeon Quest Reborn : Walkthrough Complet Winter Outpost",
    "best-equipment-for-warrior": "Dungeon Quest Reborn : Meilleur Équip du Guerrier Guide",
    "best-equipment": "Dungeon Quest Reborn : Meilleur Équip du Jeu Ranked Guide",
    "equipment-glitches": "Dungeon Quest Reborn : Glitches Équipement et Solutions Jeu",
    "equipment-level-requirements": "Dungeon Quest Reborn : Niveaux Requis Équipement Guide",
    "equipment-meta": "Dungeon Quest Reborn : Méta Actuel de l'Équipement du Jeu",
    "equipment-stat-priority": "Dungeon Quest Reborn : Priorité Stats Équip Guide Jeu",
    "event-equipment": "Dungeon Quest Reborn : Équipement des Événements du Jeu",
    "physical-power-gear": "Dungeon Quest Reborn : Équip Pouvoir Physique Complet Guide",
    "beginner-guide": "Dungeon Quest Reborn : Guide Complet pour Débutants du Jeu",
    "best-farming-spots": "Dungeon Quest Reborn : Meilleurs Spots Farm du Jeu Guide",
    "drop-rate-guide": "Dungeon Quest Reborn : Guide Complet des Taux de Drop Jeu",
    "how-to-clear-dungeons-fast": "Dungeon Quest Reborn : Clear Donjons Rapide Guide Complet",
    "how-to-compare-equipment": "Dungeon Quest Reborn : Comment Comparer l'Équip du Jeu",
    "how-to-level-fast": "Dungeon Quest Reborn : Monter Niveau Très Vite Guide Jeu",
    "how-to-unlock-winter-outpost": "Dungeon Quest Reborn : Débloquer Winter Outpost du Jeu",
    "season-guide": "Dungeon Quest Reborn : Guide Complet de Saison du Jeu",
    "speed-run-guide": "Dungeon Quest Reborn : Guide Complet Speed Run du Jeu",
    "when-to-move-to-next-dungeon": "Dungeon Quest Reborn : Quand Changer de Donjon du Jeu",
    "best-spells": "Dungeon Quest Reborn : Meilleurs Sorts du Jeu Tier Guide",
    "how-to-get-rare-spells": "Dungeon Quest Reborn : Obtenir Sorts Rares du Jeu Guide",
    "spell-animation-guide": "Dungeon Quest Reborn : Guide Animations des Sorts du Jeu",
    "spell-area-of-effect": "Dungeon Quest Reborn : Zone Effet Sorts du Jeu Guide",
    "spell-comparison": "Dungeon Quest Reborn : Comparaison Sorts DPS du Jeu Guide",
    "spell-drop-locations": "Dungeon Quest Reborn : Drops Sorts et Locations du Jeu",
    "spell-level-requirements": "Dungeon Quest Reborn : Niveaux Requis pour Sorts du Jeu",
    "spell-meta": "Dungeon Quest Reborn : Méta Actuel Sorts du Jeu Guide",
    "best-overall-tier-list": "Dungeon Quest Reborn : Meilleure Tier List Générale du Jeu",
    "c-tier-weapons": "Dungeon Quest Reborn : Armes C-Tier Liste Stats du Jeu",
    "early-game-tier-list": "Dungeon Quest Reborn : Tier List du Début du Jeu Guide",
    "tier-list-explanation": "Dungeon Quest Reborn : Explication Tier List du Jeu Guide",
    "tier-list-history": "Dungeon Quest Reborn : Historique Tier List Changements Jeu",
    "tier-list-rankings": "Dungeon Quest Reborn : Classements Complets de la Tier List",
    "tier-list-update": "Dungeon Quest Reborn : Dernière Tier List du Jeu Guide",
    "tier-list": "Dungeon Quest Reborn : Tier List Complète Rankings du Jeu",
    "community-update": "Dungeon Quest Reborn : MàJ de la Communauté du Jeu Guide",
    "major-update": "Dungeon Quest Reborn : Grosse Mise à Jour du Jeu Détails",
    "new-dungeon": "Dungeon Quest Reborn : Nouveau Donjon Guide Complet du Jeu",
    "patch-notes": "Dungeon Quest Reborn : Notes du Patch et Changements Jeu",
    "quality-of-life-update": "Dungeon Quest Reborn : Améliorations QoL du Jeu Guide",
    "roadmap": "Dungeon Quest Reborn : Roadmap du Jeu Complète et Détaillée",
    "seasonal-event": "Dungeon Quest Reborn : Événement de Saison du Jeu Guide",
    "update-review": "Dungeon Quest Reborn : Review de la Mise à Jour du Jeu",
    "best-dagger": "Dungeon Quest Reborn : Meilleures Dagues Classement DPS Jeu",
    "best-weapon-for-farming": "Dungeon Quest Reborn : Meilleure Arme Farm du Jeu Guide",
    "best-weapons": "Dungeon Quest Reborn : Meilleures Armes du Jeu Tier Guide",
    "legendary-weapons-list": "Dungeon Quest Reborn : Armes Légendaires Liste Guide Jeu",
    "pirate-island-weapons": "Dungeon Quest Reborn : Armes Île des Pirates du Jeu Guide",
    "unobtainable-weapons": "Dungeon Quest Reborn : Armes Inobtenibles Liste du Jeu Guide",
    "weapon-market": "Dungeon Quest Reborn : Marché des Armes Trading du Jeu Guide",
    "weapon-upgrade-cost": "Dungeon Quest Reborn : Coût Upgrade Armes du Jeu Guide",
}

# Fix typos
FR_TITLES = {k: v.replace("'", "É") for k, v in FR_TITLES.items()}

err = 0
for slug, t in FR_TITLES.items():
    if len(t) < 50 or len(t) > 60:
        print(f"FR FAIL {len(t)}c: {slug}")
        err += 1
if err == 0:
    print(f"FR titles OK ({len(FR_TITLES)} entries)")


PT_TITLES = {
    "boss-guide": "Dungeon Quest Reborn: Guia Completo de Todos os Chefes",
    "boss-comparison": "Dungeon Quest Reborn: Comparação de Chefes e Drops Guia",
    "boss-enrage-timer": "Dungeon Quest Reborn: Timer Enfado dos Chefes Guia",
    "boss-health-guide": "Dungeon Quest Reborn: HP e Fraquezas de Cada Chefe",
    "boss-rush-guide": "Dungeon Quest Reborn: Modo Boss Rush Guia Completa",
    "easiest-boss": "Dungeon Quest Reborn: Chefe Mais Fácil e Como Vencer",
    "how-to-beat-bosses-solo": "Dungeon Quest Reborn: Derrotar os Chefes Solo Guia",
    "how-to-beat-winter-outpost-boss": "Dungeon Quest Reborn: Guia Chefe do Winter Outpost",
    "class-exclusive-gear": "Dungeon Quest Reborn: Equipamento Exclusivo por Classe",
    "class-guide": "Dungeon Quest Reborn: Guerreiro vs Mago Guia Completo",
    "class-specific-dungeons": "Dungeon Quest Reborn: Masmorras Exclusivas por Classe",
    "class-tier-list": "Dungeon Quest Reborn: Tier List de Classes Completa",
    "hybrid-build": "Dungeon Quest Reborn: Melhor Build Híbrida do Jogo",
    "warrior-ability-rotation": "Dungeon Quest Reborn: Rotação Habilidades Guerreiro",
    "warrior-stat-priority": "Dungeon Quest Reborn: Prioridade Stats Guerreiro Guia",
    "warrior-tips": "Dungeon Quest Reborn: Dicas Avançadas do Guerreiro Jogo",
    "desert-temple-guide": "Dungeon Quest Reborn: Guia Templo do Deserto Completo",
    "dungeon-armor-drops": "Dungeon Quest Reborn: Drops Armadura Masmorras Guia",
    "dungeon-difficulty-levels": "Dungeon Quest Reborn: Níveis de Dificuldade Masmorras",
    "dungeon-layout-guide": "Dungeon Quest Reborn: Layout de Todas as Masmorras Guia",
    "dungeon-ranking": "Dungeon Quest Reborn: Ranking de Todas as Masmorras Guia",
    "dungeon-tier-list": "Dungeon Quest Reborn: Tier List de Masmorras do Jogo",
    "pirate-island-boss": "Dungeon Quest Reborn: Guia Chefe da Ilha dos Piratas",
    "winter-outpost-walkthrough": "Dungeon Quest Reborn: Walkthrough de Winter Outpost Guia",
    "best-equipment-for-warrior": "Dungeon Quest Reborn: Melhor Equip do Guerreiro Jogo",
    "best-equipment": "Dungeon Quest Reborn: Melhor Equip de Todo o Jogo Ranked",
    "equipment-glitches": "Dungeon Quest Reborn: Glitches Equipamento e Soluções",
    "equipment-level-requirements": "Dungeon Quest Reborn: Níveis Requeridos Equip Guia",
    "equipment-meta": "Dungeon Quest Reborn: Meta Atual Equipamento do Jogo",
    "equipment-stat-priority": "Dungeon Quest Reborn: Prioridade Stats Equip do Jogo",
    "event-equipment": "Dungeon Quest Reborn: Equipamento Eventos e Rewards Guia",
    "physical-power-gear": "Dungeon Quest Reborn: Equip Poder Físico Completo Guia",
    "beginner-guide": "Dungeon Quest Reborn: Guia Iniciantes do Jogo Completo",
    "best-farming-spots": "Dungeon Quest Reborn: Melhores Spots Farm e XP Jogo",
    "drop-rate-guide": "Dungeon Quest Reborn: Guia Drop Rates do Jogo Atual",
    "how-to-clear-dungeons-fast": "Dungeon Quest Reborn: Limpar Masmorras Rápido Guia",
    "how-to-compare-equipment": "Dungeon Quest Reborn: Como Comparar Equipamento Guia",
    "how-to-level-fast": "Dungeon Quest Reborn: Subir Nível Rápido do Jogo Guía",
    "how-to-unlock-winter-outpost": "Dungeon Quest Reborn: Desbloquear Winter Outpost Guia",
    "season-guide": "Dungeon Quest Reborn: Guia de Temporada Detalhada Jogo",
    "speed-run-guide": "Dungeon Quest Reborn: Guia Speed Run do Jogo Completo",
    "when-to-move-to-next-dungeon": "Dungeon Quest Reborn: Quando Trocar de Masmorra Guia",
    "best-spells": "Dungeon Quest Reborn: Melhores Feitiços Tier do Jogo",
    "how-to-get-rare-spells": "Dungeon Quest Reborn: Conseguir Feitiços Raros Guia",
    "spell-animation-guide": "Dungeon Quest Reborn: Animações Feitiços do Jogo Guia",
    "spell-area-of-effect": "Dungeon Quest Reborn: Área de Efeito Feitiços Guia",
    "spell-comparison": "Dungeon Quest Reborn: Comparação Feitiços e DPS Guia",
    "spell-drop-locations": "Dungeon Quest Reborn: Drops Feitiços Localizações Guia",
    "spell-level-requirements": "Dungeon Quest Reborn: Níveis Requeridos Feitiços Guia",
    "spell-meta": "Dungeon Quest Reborn: Meta Atual de Feitiços do Jogo",
    "best-overall-tier-list": "Dungeon Quest Reborn: Melhor Tier List Geral do Jogo",
    "c-tier-weapons": "Dungeon Quest Reborn: Armas C-Tier Lista e Stats Guia",
    "early-game-tier-list": "Dungeon Quest Reborn: Tier List Início do Jogo Guia",
    "tier-list-explanation": "Dungeon Quest Reborn: Como Funciona a Tier List Guía",
    "tier-list-history": "Dungeon Quest Reborn: Histórico Mudanças na Tier List",
    "tier-list-rankings": "Dungeon Quest Reborn: Rankings Completos da Tier List",
    "tier-list-update": "Dungeon Quest Reborn: Última Tier List do Jogo Guia",
    "tier-list": "Dungeon Quest Reborn: Tier List Completa e Rankings Jogo",
    "community-update": "Dungeon Quest Reborn: Update da Comunidade do Jogo",
    "major-update": "Dungeon Quest Reborn: Grande Atualização Detalhada Jogo",
    "new-dungeon": "Dungeon Quest Reborn: Nova Masmorra Guia do Jogo Completo",
    "patch-notes": "Dungeon Quest Reborn: Notas do Patch e Mudanças Guia",
    "quality-of-life-update": "Dungeon Quest Reborn: Melhorias QoL de Todo o Jogo",
    "roadmap": "Dungeon Quest Reborn: Roadmap do Jogo Completo Guia",
    "seasonal-event": "Dungeon Quest Reborn: Evento Temporada Guia do Jogo",
    "update-review": "Dungeon Quest Reborn: Review da Atualização do Jogo Guia",
    "best-dagger": "Dungeon Quest Reborn: Melhores Adagas Ranking do Jogo",
    "best-weapon-for-farming": "Dungeon Quest Reborn: Melhor Arma pra Farming Guia",
    "best-weapons": "Dungeon Quest Reborn: Melhores Armas do Jogo Tier Ranked",
    "legendary-weapons-list": "Dungeon Quest Reborn: Lista Armas Lendárias Completa",
    "pirate-island-weapons": "Dungeon Quest Reborn: Armas Ilha dos Piratas do Jogo",
    "unobtainable-weapons": "Dungeon Quest Reborn: Armas Inobteníveis Lista Completa",
    "weapon-market": "Dungeon Quest Reborn: Mercado de Armas Trading Guia",
    "weapon-upgrade-cost": "Dungeon Quest Reborn: Custo Upgrade Armas do Jogo Guia",
}

err = 0
for slug, t in PT_TITLES.items():
    if len(t) < 50 or len(t) > 60:
        print(f"PT FAIL {len(t)}c: {slug}")
        err += 1
if err == 0:
    print(f"PT titles OK ({len(PT_TITLES)} entries)")


def extract_metadata_slug(content):
    m = re.search(r'slug:\s*["\x27]?([^"\x27\n,]+)["\x27]?', content)
    return m.group(1).strip().strip('"').strip("'") if m else None


def replace_field(content, field_name, new_value):
    """Replace title or description in MDX metadata."""
    # Match field: "value" or field: 'value' with optional trailing comma
    pat = rf'^(\s*{field_name}:\s*)(["\x27])(.+?)\2\s*,?\s*$'
    m = re.search(pat, content, re.MULTILINE)
    if m:
        quote_char = m.group(2)
        prefix = m.group(1)
        escaped = new_value.replace('"', '\"')
        quoted = quote_char + escaped + quote_char
        new_full = prefix + quoted
        return content.replace(m.group(0), new_full, 1), True
    # Fallback: field without quotes
    pat2 = rf'^(\s*{field_name}:\s*)([^,\n]+?)\s*,?\s*$'
    m2 = re.search(pat2, content, re.MULTILINE)
    if not m2:
        return content, False
    prefix = m2.group(1)
    escaped = new_value.replace('"', '\"')
    quoted = '"' + escaped + '"'
    new_full = prefix + quoted
    return content.replace(m2.group(0), new_full, 1), True


# Description caches loaded from JSON
import json as _json
_DESC_CACHE_PATH = Path(__file__).parent / "desc_cache.json"
_DESC_CACHE = {}
if _DESC_CACHE_PATH.exists():
    with open(_DESC_CACHE_PATH, encoding="utf-8") as _f:
        _DESC_CACHE = _json.load(_f)


def main():
    lang_maps = {
        "en": EN_TITLES,
        "es": ES_TITLES,
        "fr": FR_TITLES,
        "pt": PT_TITLES,
    }

    total_updated = 0
    total_skipped = 0

    for lang in ["en", "es", "fr", "pt"]:
        lang_dir = CONTENT_DIR / lang
        if not lang_dir.exists():
            print(f"[SKIP] {lang_dir} does not exist")
            continue

        title_map = lang_maps[lang]
        # EN has descriptions in EN_DESCS; ES/FR/PT use desc_cache.json
        if lang == "en":
            desc_map = EN_DESCS
        else:
            desc_map = _DESC_CACHE.get(lang, {})

        mdx_files = sorted(lang_dir.rglob("*.mdx"))
        print(f"Processing {lang}/: {len(mdx_files)} MDX files")

        updated = 0
        skipped = 0
        for fpath in mdx_files:
            content = fpath.read_text(encoding="utf-8")
            slug = extract_metadata_slug(content)
            if slug is None:
                print(f"  [WARN] No slug in {fpath.name}")
                skipped += 1
                continue
            if slug not in title_map:
                print(f"  [WARN] No title for slug '{slug}' in {lang}")
                skipped += 1
                continue

            new_title = title_map[slug]
            content, ok = replace_field(content, "title", new_title)
            if not ok:
                print(f"  [ERROR] Could not replace title in {fpath.name}")
                skipped += 1
                continue
            # Also update description
            if slug in desc_map:
                content, ok2 = replace_field(content, "description", desc_map[slug])
                if not ok2:
                    print(f"  [ERROR] Could not replace description in {fpath.name}")
            fpath.write_text(content, encoding="utf-8")
            updated += 1

        print(f"  Summary: {updated} updated, {skipped} skipped")
        total_updated += updated
        total_skipped += skipped

    print(f"Total: {total_updated} updated, {total_skipped} skipped")


if __name__ == "__main__":
    main()
