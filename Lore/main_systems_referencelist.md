# Sinveil Gameplay Systems Reference List

Comprehensive index of gameplay systems an AI Game Master must understand. Each entry lists the system name, Order Number (reference ID used in cross-references), source JSON file, and a brief description.

## Main Lorebook (`Lorebooks/sinveil_lorebook_main_v5.json`)

| System                   | Order Number | Description                                               |
| ------------------------ | ------------ | --------------------------------------------------------- |
| Technique Rarity System  | 285          | Technique tier progression from Common to Divine.         |
| Bloodline System & Tiers | 290          | Bloodline power levels from Mortal to Primordial.         |
| MC Bloodline Evolution   | 725          | How the protagonist's bloodline awakens at breakthroughs. |

## Game Systems Lorebook (`Lorebooks/sinveil_lorebook_game_systems_v7.json`)

### Companion & Party Systems

| System                            | Order Number | Description                                                  |
| --------------------------------- | ------------ | ------------------------------------------------------------ |
| Procedural Companion Generation   | 490          | Rules for creating unique followers procedurally.            |
| Motivation Library                | 494          | Catalog of reasons companions choose to follow the MC.       |
| Speech Pattern Library            | 495          | Dialogue style references to diversify NPC voices.           |
| Secret Library                    | 496          | Hidden truths revealed at loyalty 60+ for companions.        |
| Flaw Library                      | 497          | Bank of flaws to make companions memorable.                  |
| Personality Trait Library         | 498          | Core trait options for quickly defining personalities.       |
| Universal Companion Template      | 499          | Base template applied to all recruitable NPCs.               |
| Core Companion System - Framework | 493          | Party composition rules and companion management.            |
| NPC Generation Rules              | 508          | Path matching and terminology guidelines for new NPCs.       |
| Companion Signature Equipment     | 572          | How companions acquire and upgrade their signature gear.     |
| Companion Breakthrough Events     | 570          | Realm advancement milestones and event hooks for companions. |
| Companion Loyalty-Gated Abilities | 571          | Powers unlocked as loyalty thresholds are reached.           |
| Companion Combat AI               | 573          | Behavioral guidance for allies during battles.               |
| Companion Loyalty System          | 581          | Loyalty mechanics and tier effects (0-100 scale).            |
| Romance System                    | 580          | Romance progression stages and requirements.                 |
| Death and Revival System          | 579          | Rules for character death and resurrection options.          |
| Camp Master Event Trigger         | 2000         | Base condition for launching camp vignette sequences.        |
| Camp Training Vignettes           | 2001         | Training scene prompts for bonding or growth.                |
| Camp Conflict Vignettes           | 2002         | Disagreement scenes that challenge party dynamics.           |
| Camp Bonding Vignettes            | 2003         | Quiet moments that deepen relationships.                     |
| Camp Discovery Vignettes          | 2004         | Exploration interludes revealing clues or lore.              |
| Camp Request Vignettes            | 2005         | Companion asks or favors presented during downtime.          |
| Camp Life Vignettes               | 2006         | Everyday camp flavor scenes to keep the world alive.         |

### Combat & Action Systems

| System                            | Order Number | Description                                                      |
| --------------------------------- | ------------ | ---------------------------------------------------------------- |
| Base Combat System                | 597          | Core non-technique attack and resolution rules.                  |
| Combat Role System                | 589          | Tank, DPS, Support, Controller role definitions.                 |
| Random Encounter System           | 577          | Travel encounter generation and difficulty scaling.              |
| Health Points System              | 598          | Defines HP handling and recovery fundamentals.                   |
| Stamina System                    | 596          | Stamina costs, exhaustion, and recovery.                         |
| Qi Pool System                    | 723          | Qi resource management and technique costs.                      |
| Injury Status System              | 629          | Four-tier lasting injury rules separate from HP.                 |
| Combat Healing Items System       | 630          | Usage rules for consumables during and after combat.             |
| Healer Camp Follower Mechanics    | 631          | How healer companions accelerate recovery and support the party. |
| Standard Enemy Stat Matrix        | 613          | Baseline stats for enemies by realm and tier.                    |
| Mob Behavior Scripts              | 612          | AI tactical scripts for enemy combat behavior.                   |
| Combat Terrain & Hazards          | 611          | Environmental modifiers and hazard system.                       |
| Hazard Glossary                   | 610          | Definitions and triggers for common battlefield hazards.         |
| Combat Formulas Quick Reference   | 625          | Canonical math for damage, defense, and accuracy calculations.   |
| Crippled Injury Types Table       | 6291         | Randomized severe injury results (1d8) and effects.              |
| MC Primordial Injury Protection   | 6292         | How the protagonist's bloodline mitigates crippling wounds.      |
| Combat Healing Usage Limits       | 6301         | Restrictions on healing item use per encounter.                  |
| Injury Recovery Items             | 6302         | Consumables that accelerate healing of injuries.                 |
| Purification Items                | 6303         | Items that reduce corruption accumulation.                       |
| Healer Active Treatment Mechanics | 6311         | How healer actions accelerate recovery.                          |
| Healer Supplies and Loyalty       | 6312         | Resource and loyalty impacts on healer effectiveness.            |

### Domain Combat (Astral+ Realm)

| System                                | Order Number | Description                                             |
| ------------------------------------- | ------------ | ------------------------------------------------------- |
| Domain Combat System - Core           | 750          | Domain clash mechanics for Astral realm and above.      |
| Domain Clash Resolution               | 751          | How domain strength is calculated and compared.         |
| Domain Controller Bonuses             | 752          | Advantages gained by the domain controller.             |
| Domain Qi Costs & Maintenance         | 753          | Resource drain for maintaining domains.                 |
| Domain Quick Reference                | 749          | Cheat sheet for domain combat rules.                    |
| Domain Interactions and Special Cases | 755          | Edge cases and cross-domain effects to resolve clashes. |
| Domain Narrative Descriptions         | 756          | Flavor guidance for describing domain manifestations.   |
| Orthodox Artifact Domain Enhancement  | 757          | Domain bonuses tied to orthodox artifact wielders.      |

### Technique & Cultivation Systems

| System                          | Order Number | Description                                                 |
| ------------------------------- | ------------ | ----------------------------------------------------------- |
| Technique Mastery System        | 590          | 0-100% mastery progression and breakthrough mechanics.      |
| Technique Slot System           | 591          | Technique capacity by realm and bloodline.                  |
| Breakthrough System             | 583          | Realm advancement requirements and tribulations.            |
| Breakthrough Aftermath Protocol | 5831         | 7-step post-tribulation checklist: narration, evolution, unlocks, recovery. |
| Leveling and Stat Points System | 599          | Explains advancement pacing and point distribution.         |
| Core Stats System               | 600          | Details the primary attributes and their mechanical impact. |
| Transcendence System            | 820          | Stat overflow conversion and high-realm growth.             |
| Transcendent Stats              | 821          | Categories and effects for transcendence attributes.        |
| Transcendence Builds            | 822          | Allocation strategies for transcendence points.             |
| Enemy Transcendence             | 823          | Domain power adjustments for enemy units.                   |
| Transcendence Quick Reference   | 824          | Summary of transcendence rules for fast lookup.             |
| Cultivation Speed & Progress    | 586          | How cultivation pace and breakthroughs are calculated.      |
| Difficulty Modes                | 578          | Player-facing scaling options and their mechanical impact.  |

### Corruption System

| System                                          | Order Number | Description                                               |
| ----------------------------------------------- | ------------ | --------------------------------------------------------- |
| Corruption System                               | 595          | Core corruption mechanics and percentage tracking.        |
| Corruption Tutorial: Overview                   | 632          | Introduces corruption stakes and narrative framing.       |
| Corruption Tutorial: Sources                    | 633          | Lists how corruption is gained during play.               |
| Corruption Tutorial: Thresholds & Effects       | 634          | Breakpoints and consequences for corruption accumulation. |
| Corruption Tutorial: Purification               | 635          | Methods to reduce corruption and their costs.             |
| Corruption Tutorial: Strategic Considerations   | 636          | Guidance on when to risk or manage corruption.            |
| Corruption Tutorial: First Encounter Guidelines | 637          | Steps for running a player's first corruption temptation. |

### Reputation & Standing Systems

| System                          | Order Number | Description                                                      |
| ------------------------------- | ------------ | ---------------------------------------------------------------- |
| Notoriety System                | 592          | Tracks fame/infamy escalation and related triggers for factions. |
| Sect Standing System            | 593          | Measures reputation tiers within sect hierarchies.               |
| Sect Contribution Points System | 718          | Earning and spending contribution points within sects.           |
| Notoriety System (Deprecated)   | 651          | Legacy notoriety reference replaced by Order 592.                |

### Economy & Equipment Systems

| System                              | Order Number | Description                                              |
| ----------------------------------- | ------------ | -------------------------------------------------------- |
| New Economic System                 | 700          | Wealth tiers, transaction rules, and pricing.            |
| Economic Tier System                | 708          | Solves currency scaling with tiered purchasing power.    |
| Economic Item Cost Tiers            | 701          | Tiered price reference for common items and services.    |
| Wealth Points System                | 709          | Handling major purchases and wealth abstractions.        |
| Reference - Typical Wealth by Realm | 694          | Baseline wealth expectations for each cultivation realm. |
| Reference - Services Pricing        | 695          | Standardized service costs tied to tiers.                |
| Reference - Equipment Pricing       | 696          | Tier-based equipment cost guidance.                      |
| Reference - Technique Pricing       | 697          | Pricing tiers for manuals and techniques.                |
| Reference - Cultivation Resources   | 698          | Resource costs by realm for cultivation needs.           |
| Inventory and Equipment System      | 588          | Storage, spatial rings, and equipment management.        |
| Equipment Slot Clarifications       | 6316         | Slot rules and limitations for equipped items.           |
| Weapon Damage Baseline & Scaling    | 6317         | Damage baselines and scaling for weapons and techniques. |
| Legendary Item Attunement System    | 6313         | Limits and process for attuning legendary gear.          |
| Equipment Notoriety System          | 6314         | Notoriety impacts from wielding notable equipment.       |
| Stat Cap Exceptions for Legendaries | 6315         | Cases where legendary gear alters stat ceilings.         |
| Legendary Artifact Index            | 6318         | Catalog of named legendary artifacts and references.     |

### Sin Artifact System

| System                                   | Order Number | Description                                         |
| ---------------------------------------- | ------------ | --------------------------------------------------- |
| Sin Artifact Bonding - Core              | 710          | How Sin Artifacts bond and progress through stages. |
| Sin Artifact Domain System               | 711          | Domain formula, multipliers, effects, and General artifact status. |
| Current General Artifact Status          | 712          | Which Generals have what artifact stage.            |
| Sin Artifact Signature Abilities         | 713          | Unique powers of each Sin Artifact.                 |
| Claiming Sin Artifacts - Mortal          | 714          | How the MC can claim and use Sin Artifacts.         |
| Artifact Bonding Progression             | 715          | How to accelerate artifact mastery.                 |
| Fighting Sin Artifact Wielders           | 716          | Tactics for battling artifact-empowered enemies.    |
| Artifact Destruction and Sealing         | 717          | Methods to destroy or seal Sin Artifacts.           |

### Crafting & Professions

| System                                | Order Number | Description                                           |
| ------------------------------------- | ------------ | ----------------------------------------------------- |
| Crafting System Overview              | 587          | Alchemy, blacksmithing, and formation array basics.   |
| Profession System                     | 798          | Profession skills, progression, and crafting basics.  |
| Material Tier System                  | 799          | Complete list of crafting materials by tier.          |
| Crafting Generation Protocol          | 800          | Primary system for generating crafted items.          |
| Crafting Bonuses & Special Conditions | 794          | Situational modifiers that alter crafting outcomes.   |
| Crafting Economics                    | 795          | Guidance on acquiring and valuing crafting materials. |
| Example Recipes                       | 796          | Templates for notable pills, talismans, and arrays.   |
| Special Traits - Superior/Perfect     | 797          | Quality traits and their effects on crafted goods.    |
| Sect Interaction Module               | 719          | Sect-specific resources and mission archetypes.       |
| Sect Facilities & Bronze Access       | 727          | Facility costs, realm restrictions, disciple tiers.   |
| Recipe Compendium                     | 726          | Standard recipes for pills, talismans, and arrays.    |

### Quest & Progression Systems

| System                         | Order Number | Description                                               |
| ------------------------------ | ------------ | --------------------------------------------------------- |
| Quest System                   | 582          | Quest types, tracking, and reward structures.             |
| Downtime System                | 584          | Training, rest, and meditation between adventures.        |
| Fate's Gambit System           | 594          | Custom player actions outside standard options.           |
| Treasure and Reward Guidelines | 693          | Tables and principles for loot and rewards.               |
| Quest Generation Template      | 720          | Structure for building new quests with consistent pacing. |
| Item/Loot Generation Template  | 721          | Framework for producing balanced loot drops.              |
| Equipment Acquisition Methods  | 722          | Ways characters can legitimately obtain equipment.        |

### Character Perks

| System                             | Order Number | Description                                             |
| ---------------------------------- | ------------ | ------------------------------------------------------- |
| Character Perks - Overview         | 850          | Perk acquisition sources and limits (10 max).           |
| Character Perks - Combat           | 851          | Combat-focused permanent bonuses.                       |
| Character Perks - Social & Utility | 852          | Non-combat perks for exploration and social encounters. |
| Character Perks - Cultivation      | 853          | Cultivation and corruption-focused perks.               |

### Artifact Catalogs

| Artifact                                     | Order Number | Description                                                |
| -------------------------------------------- | ------------ | ---------------------------------------------------------- |
| Legendary Artifact: Atlas Mantle             | 6320         | Legendary defensive mantle with world-anchoring powers.    |
| Legendary Artifact: Celestial Halo           | 6321         | Radiant halo artifact with protective blessings.           |
| Legendary Artifact: Dawnbringer Hammer       | 6322         | Myth-forged hammer channeling dawnfire might.              |
| Legendary Artifact: Earthshaker Gauntlets    | 6323         | Gauntlets that amplify seismic strength.                   |
| Legendary Artifact: Fist of the Immortal     | 6324         | Martial fist weapon that immortalizes strikes.             |
| Legendary Artifact: Frozen Heart Amulet      | 6325         | Amulet that preserves calm and ice-aligned qi.             |
| Legendary Artifact: Heaven's Decree          | 6326         | Divine writ blade enforcing celestial judgment.            |
| Legendary Artifact: Muramasa                 | 6327         | Cursed blade with insatiable edge.                         |
| Legendary Artifact: Phoenix Crown of Rebirth | 6328         | Crown granting rebirth flames and vitality.                |
| Legendary Artifact: Shadowfang Dagger        | 6329         | Stealth dagger that devours light and sound.               |
| Legendary Artifact: Stormcaller's Mantle     | 6330         | Cloak that commands tempests and wind currents.            |
| Legendary Artifact: Tidekeeper's Trident     | 6331         | Trident that governs tides and marine qi.                  |
| Legendary Artifact: Titan's Aegis            | 6332         | Shield imbued with titan durability.                       |
| Legendary Artifact: Voidweaver Robes         | 6333         | Robes that warp spatial flows for protection.              |
| Legendary Artifact: Worldbreaker Greatsword  | 6334         | Greatsword capable of sundering landscapes.                |
| Legendary Artifact: Zephyr Blade             | 6335         | Swift blade that rides and shapes the wind.                |
| Mythic Artifact Tier Overview                | 6340         | Overview of mythic-tier artifact expectations and effects. |
| Mythic Artifact: Stormbreaker                | 6341         | Mythic weapon that commands storms.                        |
| Mythic Artifact: Tidecrown                   | 6342         | Crown channeling oceanic dominance.                        |
| Mythic Artifact: Worldsplitter               | 6343         | Weapon capable of cleaving realms.                         |
| Mythic Artifact: Phoenix Heart               | 6344         | Core that fuels eternal phoenix fire.                      |
| Mythic Artifact: Eclipse Blade               | 6345         | Blade harnessing light-and-shadow balance.                 |
| Mythic Artifact: Heavenfall                  | 6346         | Meteoric weapon invoking falling heavens.                  |
| Mythic Artifact: Soulreaver                  | 6347         | Weapon that harvests souls to grow stronger.               |
| Mythic Artifact: Titanform                   | 6348         | Artifact that grants titanic transformation.               |
| Divine Artifact Tier Overview                | 6350         | Overview of divine-tier artifact scale and rarity.         |
| Divine Artifact: Titan's Mantle              | 6351         | King Titan's mantle that magnifies domain might.           |
| Divine Artifact: Umbral Veil                 | 6352         | Lady Umbra's veil for supreme stealth and shadow control.  |
| Divine Artifact: Tidemother's Pearl          | 6353         | Lady Maren's pearl that commands oceans.                   |
| Divine Artifact: Pyrrhus' Ember              | 6354         | Lord Pyrrhus's ember fueling catastrophic fire.            |
| Divine Artifact: Tempest Crown               | 6355         | Lord Aethon's crown of absolute storms.                    |
| Divine Artifact: Radiant Halo                | 6356         | Lady Solara's halo radiating cleansing light.              |
| Divine Artifact: Mind's Eye                  | 6357         | Sage Veritas's artifact granting perfect insight.          |
| Divine Artifact: Warlord's Banner            | 6358         | Lord Vexar's banner empowering armies.                     |
| Mythic Artifact: Sunpiercer                  | 6360         | Light-aspected bow that pierces sunfire arrows.            |
| Mythic Artifact: Godhand Wraps               | 6361         | Body-aspected wraps for unstoppable strikes.               |
| Mythic Artifact: Inferno Lotus               | 6362         | Fire-aspected lotus amplifying flame arts.                 |
| Divine Artifact: Abyssal Pearl               | 6363         | Lord of the Depths' pearl manipulating abyssal waters.     |
| Divine Artifact: Monolith of Silence         | 6364         | Lord of Silence's monolith that suppresses sound and qi.   |

### Living World Engine

| System                              | Order Number | Description                                               |
| ----------------------------------- | ------------ | --------------------------------------------------------- |
| Living World Engine - Core          | 650          | Monthly campaign pressure loop and systemic updates.      |
| General Accumulation System         | 652          | Tracks Sin Generals' power growth over time.              |
| Inter-General Conflict System       | 653          | Rules for rivalries and clashes between Generals.         |
| Regional Threat Level System        | 654          | Establishes danger ratings per region.                    |
| Victory and Defeat Conditions       | 655          | Win/loss criteria for the campaign arc.                   |
| Monthly World Update Protocol       | 656          | Procedure for processing world changes each month.        |
| General Realm Breakthrough          | 657          | Advancement checks and outcomes for Generals.             |
| General Monthly Action Tables       | 658          | Activity tables guiding General behavior each cycle.      |
| General Behavior - Pride (Vaelen)   | 660          | AI behavior script for the Pride General.                 |
| General Behavior - Greed (Aurex)    | 661          | AI behavior script for the Greed General.                 |
| General Behavior - Temptation       | 662          | AI behavior script for the Temptation General.            |
| General Behavior - Envy (Elowen)    | 663          | AI behavior script for the Envy General.                  |
| General Behavior - Gluttony (Glut)  | 664          | AI behavior script for the Gluttony General.              |
| General Behavior - Wrath (Calderon) | 665          | AI behavior script for the Wrath General.                 |
| General Behavior - Sloth (Morvane)  | 666          | AI behavior script for the Sloth General.                 |
| World State Data Bank Schema        | 667          | Data structure for tracking world status across sessions. |
| Lieutenant System & Named Roster    | 668          | Rules for lieutenants, their roles, and roster usage.     |
| World News Delivery Guidelines      | 669          | How to present world events and rumors to players.        |
| New Game Initialization             | 670          | Starting state setup for new campaigns.                   |
| First Session Protocol              | 671          | Post-creation opening scene, tutorial gate, and pacing.   |

### Deprecated/Reference Only

| System                           | Order Number | Description                                |
| -------------------------------- | ------------ | ------------------------------------------ |
| DEPRECATED - Old Currency System | 585          | Legacy currency for flavor reference only. |

## Character Systems Lorebook (`Lorebooks/sinveil_lorebook_character_systems_v3.json`)

| System                       | Order Number | Description                                           |
| ---------------------------- | ------------ | ----------------------------------------------------- |
| Character Creation Overview  | 9999         | Full 13-stage character creation workflow.            |
| Parent Selection (Stage 1)   | 736          | Rules and options for determining lineage.            |
| Starting Technique Options   | 681          | Stage 12 technique choices by path (verified names).  |
| Relationship Tags & Loyalty  | 2011         | Tag definitions with loyalty and personality effects. |

## PC Personality Lorebook (`Lorebooks/sinveil_lorebook_pc_personality_v1.json`)

| System                                | Order Number | Description                                                |
| ------------------------------------- | ------------ | ---------------------------------------------------------- |
| PC Core Personality                   | 4000         | Foundational traits that filter choices and tone.          |
| PC Voice & Thought Patterns           | 4001         | Voice style, internal narration, and delivery cues.        |
| PC Combat & Social Philosophy         | 4002         | Preferred tactics, corruption stance, and redlines.        |
| PC Relationships & Cultivation Values | 4003         | Views on leadership, sects, and risk tolerance.            |
| PC Flaws & Background Triggers        | 4004         | Flaw hooks and triggers for authentic reactions.           |
| AI Choice Generation Master Protocol  | 4099         | Procedure for generating options that respect personality. |

## Enemies Lorebook (`Lorebooks/sinveil_lorebook_enemies_v1.json`)

| System                              | Order Number | Description                                                     |
| ----------------------------------- | ------------ | --------------------------------------------------------------- |
| Enemy Variety System Overview       | 9000         | Framework for encounter diversity and enemy roles.              |
| Rapid Companion Generation Template | 9520         | Template for converting defeated enemies into companions.       |
| Enemy-to-Companion Workflow         | 9530         | Steps for efficiently adapting enemies into recruitable allies. |
