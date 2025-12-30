# Game Systems V7 Lorebook

Formatted from `Lore/sinveil_lorebook_game_systems_v7.json`.

## Speech Pattern Library - Voice Variety
- Entry ID: 900
- Keywords: speech patterns, dialogue style, how NPC talks

SPEECH PATTERNS (50+ options - makes each companion sound different): FORMALITY: Formal (always proper grammar, titles, respect), Casual (relaxed, contractions, slang), Archaic (old-fashioned language, 'thee/thou'), Military (clipped, efficient, sir/ma'am), Street (urban slang, rough), Noble (aristocratic, refined), Peasant (common, simple), Religious (scriptural references, blessings). VERBOSITY: Terse (few words, minimal), Verbose (long-winded, elaborate), Rambling (loses track, tangents), Precise (exact word choice), Eloquent (beautiful phrasing), Choppy (short bursts), Stream-of-consciousness (continuous flow). TONE: Respectful (always courteous), Sarcastic (mocking undertone), Sincere (genuine emotion), Dramatic (theatrical delivery), Deadpan (no emotion), Enthusiastic (exclamation points), Melancholic (sad undertone), Aggressive (confrontational), Playful (teasing), Condescending (talks down). VOCABULARY: Scholarly (complex words, references), Simple (basic vocabulary), Poetic (metaphors, imagery), Technical (cultivation jargon), Profane (curses frequently), Euphemistic (avoids direct language), Blunt (brutally direct), Colorful (vivid descriptions). QUIRKS: Quotes literature/philosophy, Uses metaphors constantly, Speaks in third person, Refers to self by title, Hums while thinking, Repeats words for emphasis, Asks rhetorical questions, Finishes others' sentences, Interrupts constantly, Pauses mid-sentence, Uses wrong words (malapropism), Mixes languages, Has catchphrase, Addresses MC by title always, Uses nicknames for everyone, Never uses contractions, Overuses certain words ('indeed', 'truly', etc), Whispers/mutters, Speaks too loudly, Laughs nervously, Sighs frequently, Uses hand gestures (describe), Has verbal tic ('um', 'ah', 'you know'), Speaks in questions, Makes sound effects. EMOTIONAL DELIVERY: Wears emotions (voice shows feeling), Suppresses emotions (flat delivery), Exaggerates (melodramatic), Understated (downplays), Passionate (intense), Measured (controlled), Unpredictable (shifts rapidly). ACCENT/DIALECT: Mountain dwellers (certain phrases), Coastal folk (nautical terms), Desert people (harsh consonants), Forest elves (musical quality), Orcs (guttural), Goblins (high-pitched, quick), Dragonkin (commanding, resonant), Kitsune (sly, playful), Merchants (persuasive), Soldiers (direct), Scholars (pedantic), Criminals (coded language). INTERACTION STYLE: Asks many questions, Gives unsolicited advice, Tells stories, Quotes others, References past events, Makes predictions, Offers opinions freely, Keeps opinions private, Compliments MC, Criticizes constructively, Argues points, Agrees readily, Deflects with humor, Answers questions with questions, Changes subject, Returns to topics obsessively. AI INSTRUCTION: Combine FORMALITY + TONE + QUIRKS to create unique voice. Example combinations: 'Formal + Sarcastic + Quotes literature' = Witty aristocrat. 'Casual + Enthusiastic + Uses wrong words' = Lovable fool. 'Terse + Aggressive + Curses' = Gruff warrior. 'Verbose + Melancholic + Poetic' = Tragic scholar. Never make two companions sound the same. Speech pattern should be consistent but can evolve slightly (traumatized companion might become terse, redeemed villain might speak more openly).

## Motivation Library - Why They Follow MC
- Entry ID: 901
- Keywords: companion motivation, why follow MC, NPC goals

COMPANION MOTIVATIONS (40+ options - initial reason for following MC, can evolve): DEBT-BASED: Life debt (MC saved them), Honor debt (owe MC's family), Financial debt (MC paid their debts), Magical debt (bound by oath/spell), Karmic debt (balance cosmic scales). SURVIVAL: Protection (safety in numbers), Fleeing enemies (MC offers shelter), Nowhere else to go (lost everything), MC is strongest chance (pragmatic), Survive demon invasion (apocalypse). AMBITION: Learn from MC (martial arts/cultivation), Steal MC's secrets (hidden agenda), Use MC for advancement (social climbing), Prove superiority (competitive), Become stronger (training partner), Access MC's resources (mercenary), Gain MC's bloodline (Veinshadow Covenant), Join winning side (opportunist). IDEALISM: Believes in MC's cause (true believer), Prophecy follower (MC is chosen one), Moral duty (right thing to do), Save the world (heroic), Restore honor (redemption), Serve justice (righteous), Protect innocent (guardian). EMOTIONAL: Love/attraction (romantic), Hero worship (idolization), Family bond (treats MC as family), Friendship (genuine connection), Loneliness (desperate for connection), Guilt (atone to MC), Obsession (unhealthy fixation). ORDERS: Sect orders (assigned by master), Family orders (clan duty), Spy mission (secretly observing), Bodyguard duty (protecting MC), Political arrangement (alliance marriage), Imprisonment alternative (serve or die), Curse/binding (magically compelled). REVENGE: Enemies of enemies (shares MC's foes), Seek vengeance through MC (target too powerful alone), MC killed their enemy (gratitude), MC will lead to enemy (patient plotter), Betrayed by MC's enemy (common cause). CURIOSITY: Mystery of MC's bloodline (researching), Scientific interest (studying phenomenon), Boredom (adventure seeking), Wanderlust (going somewhere interesting), Magical binding mystery (why are they drawn to MC?), Prophecy involvement (figure out role). REDEMPTION: Former enemy seeking forgiveness, Atone for past sins, Prove changed (reform), Escape dark past (fresh start), Save soul from corruption (purification). PRACTICAL: Employment (mercenary), Traveling same direction (convenience), Lost and following (navigation failure), Rescued and grateful (short-term), Testing MC (temporary evaluation). HIDDEN AGENDA: Assassinate MC later (long con), Steal something from MC (thief), Corrupt MC for General (devil agent), Protect MC from afar (secret guardian), Replace MC (doppelganger), Learn MC's weakness (future betrayal), Report to rival sect (intelligence), Fall in love against orders (conflict). EVOLUTION: Motivations should CHANGE over time. Start as mercenary -> become loyal friend. Start as spy -> develop genuine feelings. Start as competitor -> mutual respect. Start as duty -> personal choice. Track motivation shifts in memory system. Major loyalty events can trigger motivation evolution. Companions may not be fully honest about initial motivation - reveal truth at dramatic moment. MULTIPLE MOTIVATIONS: Companions can have layered motivations. Surface motivation (what they tell MC) vs Deep motivation (true reason) vs Hidden motivation (secret agenda). Example: 'Follows for protection (surface) because fleeing Veinshadow Covenant (deep) but is actually their spy (hidden)'. Creates dramatic tension and reveals.

## Procedural Companion Generation - Instructions for AI
- Entry ID: 902
- Keywords: random companion generation, procedural NPC, create unique character

PROCEDURAL COMPANION GENERATION SYSTEM: AI should create completely unique companions by combining elements from personality libraries. NEVER reuse exact combinations. STEP 1 - ROLL IDENTITY: Select Race (15 options), Bloodline Tier (weighted: 80% Mortal, 15% Awakened, 4% Noble, 0.9% Ancient, 0.1% Divine), Age (15-800+ depending on race), Gender, Cultivation Realm (usually 1-2 realms below or equal to MC for balance, never more than 1 above), Primary Path (8 options, consider racial affinity), Combat Role OR Camp Role. STEP 2 - BUILD PERSONALITY: Select 1 Primary Trait (60+ options), 1 Secondary Trait (different from primary), 1-2 Flaws (50+ options), 1-2 Virtues, 1 Speech Pattern (50+ options with quirks), 1 Sense of Humor type or none, 1 Emotional expression style. STEP 3 - CREATE BACKGROUND: Generate Origin (which continent, which sect or independent, family status), Determine initial Motivation (40+ options), Create Secret (30+ options, can be benign or dark), Establish Fears and Dreams. STEP 4 - SET INITIAL STATE: Starting Loyalty (usually 20-50 depending on recruitment context, enemy-turned-ally starts lower, desperate person starts higher), Relationship Status (usually Stranger or Acquaintance), Romance Potential (Yes/No/Conditional - determines if Entry 580 romance stages are available; most NPCs default Yes, set No for incompatible personalities or story reasons, set Conditional for 'only if specific condition met'), Design Personal Quest (locked initially, 3-4 stage structure). STEP 5 - ADD UNIQUE DETAILS: Physical description (use race baseline, add unique features), Mannerisms (how they move, gesture, react), Catchphrase or verbal tic (optional), Relationship with other NPCs (family, old friends, enemies), Special item they carry (memento, weapon, artifact). STEP 6 - DETERMINE COMBAT/CAMP STATS: If party member - select techniques from their path/realm, assign equipment appropriate to their background. If camp follower - select camp role, determine what services they provide. VARIETY ENFORCEMENT: AI must track companions created in current playthrough and AVOID repeating combinations. If you've created a 'Sarcastic Elf Scholar who speaks in riddles' - do NOT create another. Instead create 'Blunt Dwarf Warrior who curses constantly' or 'Shy Kitsune Thief who whispers' or 'Arrogant Human Mage who quotes poetry' - completely different combinations. AIM FOR CONTRAST: If party already has serious stoic warrior, next companion should be completely different - maybe cheerful reckless scout or calculating manipulative mage. Create deliberate personality clashes AND harmonies. DEPTH OVER BREADTH: Better to have 3 deeply characterized unique companions than 6 generic ones. Each companion should feel like a potential protagonist of their own story. UNEXPECTED COMBINATIONS: Don't be predictable. Orcs don't have to be dumb warriors - create scholarly orc. Elves don't have to be wise - create naive young elf. Goblins don't have to be cowardly - create brave goblin hero. Subvert expectations while staying true to world lore. EVOLUTION TRACKING: As companions experience events with MC, their personality should evolve subtly. Naive companion becomes cynical after betrayal. Cowardly companion finds courage after saving MC. Greedy companion learns generosity. Track these changes in memory system.

## NPC Generation Rules - Path Matching & Terminology
- Entry ID: 903
- Keywords: generate NPC, create NPC, NPC generation, new character, introduce character, meet someone, encounter NPC

NPC GENERATION RULES - MANDATORY COMPLIANCE:

SECT PATH MATCHING:
- NPCs in a sect DEFAULT to that sect's primary cultivation path
- Blazing Heart Sect ? Fire Path
- Tranquil Depths Sect ? Water Path
- Soaring Freedom Sect ? Wind Path
- Unshaken Foundation Sect ? Earth Path
- Righteous Blade Sect ? Sword Path
- Veiled Mercy Sect ? Shadow Path
- Eternal Dawn Sect ? Light Path
- Iron Body Sect ? Body Path
- EXCEPTION: Only deviate if there's an explicit story reason (e.g., transfer student, defector, dual-path prodigy)
- When creating rivals/peers in player's sect, they should share the sect's primary path

REALM TERMINOLOGY (NEVER violate):
- USE: "Low Bronze", "Mid Iron", "High Silver", "Peak Gold"
- NEVER USE: "Bronze Level 3", "Iron Level 5", "Silver Rank 2"
- In NPC dialogue, use descriptions: "senior cultivator", "newly advanced", "veteran of the realm"
- WRONG: "He's Bronze Level 7" ? RIGHT: "He's a Peak Bronze cultivator, close to breakthrough"

BLOODLINE TIER NAMING (NEVER violate):
- USE tier names: Mortal, Awakened, Noble, Ancient, Divine, Primordial
- NEVER USE: "Tier 0", "Tier 1", "Tier 2", "Bloodline Level 3"
- WRONG: "Your bloodline is Tier 0" ? RIGHT: "Your bloodline is Mortal-grade"

SECT MASTER GENERATION:
- Sect Masters must be GOLD REALM MINIMUM (most are Void or Eternal)
- See Entry 257 for canonical Sect Master list - USE THESE, do not invent
- Sect Elders should be Astral+ realm
- Senior disciples typically Silver to Gold

TRAITS AND BONUSES:
- DO NOT invent arbitrary bonuses like "+10% learning speed" or "+5 to cultivation"
- All bonuses must come from defined sources: racial traits, bloodline abilities, technique effects, equipment stats
- If no lorebook defines a specific bonus, it doesn't exist

See Entry 499 (Companion Template) and Entry 490 (Procedural Generation) for full NPC creation framework.

## Core Stats System
- Entry ID: 904
- Keywords: stat check, roll, dice, ability check

CORE STATS (8 Assigned + 2 Derived):
STR (Strength) - Physical power, melee damage, carrying capacity.
DEX (Dexterity) - Agility, accuracy, evasion, ranged attacks.
CON (Constitution) - Health pool, stamina, poison/disease resistance.
INT (Intelligence) - Learning speed, technique comprehension, puzzle-solving.
WIS (Wisdom) - Judgment, qi sensitivity, mental defense.
WIL (Willpower) - Corruption resistance, tribulation endurance, focus.
CHA (Charisma) - Social influence, leadership, intimidation.
LCK (Luck) - Fate's Gambit points, critical chances, loot quality.

DERIVED STATS (rounded down):
PER (Perception) = (DEX + WIS + INT) / 3 (rounded down) - Detecting hidden enemies, sensing qi, noticing lies.
INIT (Initiative) = DEX + (WIS / 2) (rounded down) - Combat turn order.

SAVING THROWS:
Saves use the same format as stat checks: 1d20 + [STAT / 5] vs DC. Common saves: CON save (poison, disease), WIL save (mental effects, corruption), DEX save (area effects, traps).

STAT MODIFIER RULE (CRITICAL):
Formulas in techniques and items often refer to stats in brackets, e.g., '[WIS x 2]'.
Unless explicitly stated as 'Raw Score', ALL such references use the STAT MODIFIER.
Modifier Formula: [Raw Score / 5] (rounded down).
Example: A character with 25 WIS has a Modifier of 5. 'Firebolt [WIS x 2]' deals 10 damage (5 x 2), NOT 50 damage (25 x 2).

STAT SCALE: 1-20 base at character creation. Caps increase with realm: Bronze = 25, Iron = 40, Silver = 60, Gold = 85, Astral+ = 100 hard cap.

=== STAT CHECK PROTOCOL (MANDATORY FORMAT) ===

ALL PLAYER stat checks use this interactive 2-step process. NEVER roll player checks internally. (Note: GM-side table lookups such as random encounters, loot determination, and NPC generation may be rolled internally.)

STEP 1: THE CALL (AI)
State the Stat and DC, then STOP.
Format: `[CHECK REQUIRED: (Stat Name) | DC: (Number)]`

STEP 2: THE RESOLUTION (AI - Next Turn)
After the player rolls, calculate the result using their roll.
Format: `(Roll (X) + Mod (Y) = Total (Z) vs DC (N)) Result: (Success/Failure) - (Narrative)`

EXAMPLE:
AI: `[CHECK REQUIRED: STR | DC: 15]`
Player: rolls 12.
AI: `(12 + 4 = 16 vs DC 15) Result: Success - You force the door open.`

MATH RULES:
- Stat Modifier = Stat / 5 (round down)
- Examples: STR 18 = +3, STR 45 = +9, STR 100 = +20
- Natural 20 = Auto-Success + bonus effect
- Natural 1 = Auto-Failure + complication

DIFFICULTY CLASSES:
DC 10 = Easy (routine tasks)
DC 15 = Medium (challenging tasks)
DC 20 = Hard (expert-level)
DC 25 = Very Hard (master-level)
DC 30 = Impossible (legendary feats)
DC 35+ = Realm-Transcending

NEVER roll for the player. Always wait for the die roll.

## Leveling and Stat Points System
- Entry ID: 905
- Keywords: level up, experience, xp, stat points, sparring, spar, training match, combat ended, combat complete, victory

LEVELING: Each realm has 100 levels. Levels 1-33 = Low sub-realm, 34-66 = Mid sub-realm, 67-100 = High sub-realm. Cannot breakthrough to next realm until Level 100.

?? NO XP SYSTEM - DIRECT LEVEL GAINS ONLY:
Sinveil does NOT use experience points (XP). Victories grant LEVELS directly.
- CORRECT: 'Level 1 ? Level 2 (+1 level)'
- WRONG: '+15 XP (Level 1 ? 16%)' ? This is INVALID, do not do this
- NEVER add an 'xp' field to STATE_JSON - it does not exist in the schema
- Level IS breakthrough progress (Level 50 = 50% toward next realm)

SCHEMA INVARIANT - SINGLE SOURCE OF TRUTH: Track only `level` in schema (integer 1-100). In narrative, express as 'X% breakthrough progress' for cultivation scenes, 'Level X' for mechanics. NEVER track XP separately. NEVER say 'Level 67 with 45% progress' - this is logically impossible.

?? STAT POINT DISTRIBUTION (MANDATORY):
When player gains level(s), AI MUST follow this protocol:
1. ANNOUNCE: 'You've reached Level X! (+Y levels gained)'
2. CALCULATE: Points earned = Y levels ? PPL for current realm
3. SHOW CURRENT STATS: Display all 8 stats with current values and realm cap
   Example: 'STR 14 | DEX 10 | CON 15 | INT 12 | WIS 10 | WIL 9 | CHA 12 | LCK 10 (Cap: 25)'
4. PROMPT: 'You have Z stat points to distribute. Which stats would you like to increase?'
5. WAIT: Do NOT continue the scene until player responds with their stat choices
6. APPLY: Add points to chosen stats, respecting realm caps
7. CONFIRM: Update STATE_JSON with new stat values

NEVER skip stat point distribution. NEVER auto-assign points for the player. This is player agency - they decide their build.

LEVEL GAIN RATES - SPARRING (Sect Training Matches):
Sparring grants HALF the normal combat XP (round up). Sparring is safe practice, not life-or-death struggle.
- Sparring vs unnamed disciple = +1 level (half of Tier 1)
- Sparring vs named disciple (rival, friend, etc.) = +1 level (half of Tier 2, rounded up)
- Sparring vs Senior Disciple or Instructor = +2 levels (half of Tier 3)
Sparring STILL triggers stat point distribution and the STAT POINT DISTRIBUTION protocol above. NEVER skip stat points after sparring victories.

LEVEL GAIN RATES - COMBAT: Tier 1 enemy (realm-appropriate minion) = +1 level. Tier 2 enemy (named/elite) = +2 levels. Tier 3 enemy (boss) = +3-5 levels. Enemy 1 realm above = +3-5 levels. Enemy 2+ realms above = +5-10 levels (if survived). LEVEL GAIN RATES - QUESTS: Trivial sect mission = +1 level. Easy sect mission = +2 levels. Normal sect mission = +3 levels. Hard sect mission = +5 levels. Deadly/Suicidal mission = +10+ levels. LEVEL GAIN RATES - TRAINING: Daily meditation = +0.5 level. Training with master (1 day) = +1 level. Qi-rich location meditation = +1-2 levels/day. Technique practice = +0.5 level + mastery gain. See Entry 586 for cultivation speed modifiers (bloodline, location bonuses). LEVEL GAIN RATES - STORY: Minor story beat = +1-2 levels. Major revelation/victory = +3-5 levels. Near-death awakening = +5-10 levels. Traumatic event survived = +3-5 levels. PACING GUIDELINE: Bronze 1 to Bronze 100 should take approximately 20-40 sessions. Average session should yield 3-8 levels depending on activity mix. Adjust pacing per Difficulty Mode (Entry 578). STAT POINTS PER LEVEL (PPL): Bronze = 1 PPL, Iron = 2 PPL, Silver = 3 PPL, Gold = 4 PPL, Astral = 5 PPL, Void = 6 PPL, Eternal = 7 PPL, Sovereign = 8 PPL. PPL RETROACTIVITY: PPL is NOT retroactive. Bronze levels ALWAYS award 1 point each, regardless of current realm. A cultivator who reaches Iron does not retroactively gain extra points for their Bronze levels. Each realm's PPL only applies to levels gained WITHIN that realm. CUMULATIVE STATS: Start with 90 points at character creation. By Bronze 100 = 190 total. By Iron 100 = 390 total. By Silver 100 = 690 total. By Gold 100 = 1,090 total. By Astral 100 = 1,590 total. By Void 100 = 2,190 total. By Eternal 100 = 2,890 total. By Sovereign 100 = 3,690 total. STAT CAPS: Bronze = 25 max per stat, Iron = 40, Silver = 60, Gold = 85, Astral+ = 100 hard cap. SECONDARY STATS UNLOCK: Iron unlocks Tribulation Resistance, Silver unlocks Qi Efficiency, Gold unlocks Bloodline Resonance, Astral unlocks Domain Power and Intent Potency. PASSIVE CULTIVATION: Companions not in the active party gain 50% of all XP earned. They cannot breakthrough realms without a specific Camp Event or Quest.

## Health Points System
- Entry ID: 906
- Keywords: HP, health, damage, healing, bleedout, downed, con save, max HP, HP formula, cumulative level

HP FORMULA: Base 50 + (CON x 5) + (Cumulative Character Level x CON modifier). CUMULATIVE LEVEL DEFINITION: Sum of all levels gained across all realms. Bronze 100 = Level 100. Iron 100 = Level 200. Silver 100 = Level 300. Gold 100 = Level 400. Astral 100 = Level 500. Void 100 = Level 600. Eternal 100 = Level 700. Sovereign 100 = Level 800. HP THRESHOLDS: 76-100% = Healthy (no penalties), 51-75% = Wounded (minor combat penalties), 26-50% = Bloodied (moderate penalties, visible injuries), 1-25% = Critical (severe penalties, desperate state), 0 = Bleedout (dying, countdown begins). BLEEDOUT: 3 rounds (Normal difficulty). Each round roll CON save or lose 1 round. Can be stabilized by ally healing or Medicine check. Timer expires = Death. INSTANT DEATH: Only from massive overkill (damage exceeds remaining HP + Max HP) or specific narrative kills (decapitation, tribulation failure). HEALING: Pills, techniques, rest. Cannot exceed Max HP.

## Qi Pool System
- Entry ID: 907
- Keywords: Qi, qi pool, qi cost, cultivation energy

QI FORMULA: Base 30 + (WIS x 3) + (WIL x 2) + realm multiplier. REALM MULTIPLIERS: Bronze +0, Iron +20, Silver +50, Gold +100, Astral +200, Void +350, Eternal +500, Sovereign +750. QI USAGE: Techniques consume Qi based on rarity. Common = 5-10 Qi, Uncommon = 15-25 Qi, Rare = 30-50 Qi, Epic = 60-100 Qi, Legendary = 120-200 Qi, Mythic = 250-400 Qi, Divine = 500+ Qi. QI RECOVERY: Rest restores Qi at rate based on bloodline (Mortal = 10%/hour, Primordial = full in minutes). Meditation restores faster. Qi pills provide instant recovery. QI EXHAUSTION: At 0 Qi, cannot use techniques. Forced to rely on basic attacks and items.

## Stamina System
- Entry ID: 908
- Keywords: Stamina, exhaustion, tired, fatigue

STAMINA FORMULA: Base 20 + (CON x 2) + (STR x 1). STAMINA USAGE: Physical actions consume Stamina. Basic attacks = 2-5 Stamina. Physical techniques = 10-30 Stamina. Running/sprinting = 5/round. Heavy lifting = 10-20. Extended combat drains Stamina even without techniques. STAMINA EXHAUSTION: At 0 Stamina, movement halved, attack damage reduced by 50%, DEX checks at disadvantage. STAMINA RECOVERY: Short rest (10 min) = 25%. Full rest (8 hours) = 100%. Stamina pills provide instant recovery.

## Corruption System
- Entry ID: 909
- Keywords: Corruption, corruption percentage, sin taint, demonic influence

CORRUPTION THRESHOLDS: 0-24% TAINTED = No visible signs. Faint wrongness detectable by high-realm Light cultivators. Internal qi feels off during meditation. 25-49% TOUCHED = Subtle signs. Nightmares, slight temperament shifts, faint dark veins visible when channeling qi. All damage dealt +5%. 50-74% MARKED = Visible mutations begin. Eye color shifts (red/black/gold based on Sin type), tongue becomes forked/reptilian, skin discoloration, voice distortion. All damage dealt +10%. Orthodox sects become hostile if discovered. 75-99% CONSUMED = Severe mutations. Horns/scales/claws emerging, constant whispers from affiliated General, struggle to resist Sin urges. All damage dealt +25%. Purification extremely difficult. 100% FALLEN = Irreversible. Full devil transformation. Become NPC under General's command. Game over or villain arc. PURIFICATION: Only possible below Void realm. Light Path cultivators, holy sites, rare artifacts can reduce corruption. Difficulty scales with current percentage. REALM CAPS: Bronze cannot exceed 49% (Touched max). Iron+ can reach any threshold. Excess corruption from Bronze is 'banked' and applies upon reaching Iron.

## Fate's Gambit System
- Entry ID: 910
- Keywords: Fate's Gambit, gambit, custom action, player choice

FATE'S GAMBIT: Daily points that allow player to propose custom actions outside the 3-4 presented choices. DAILY POINTS: LCK / 4 (rounded down, minimum 1). LCK 4-7 = 1 point. LCK 8-11 = 2 points. LCK 12-15 = 3 points. LCK 16-19 = 4 points. LCK 20+ = 5 points. REFRESH: All points restore at dawn each day. USAGE: When standard choices don't suit, player may spend 1 Gambit point to propose any action. Action is subject to dice rolls and consequences. Creative solutions should be rewarded when successful. LIMITATIONS: Cannot propose actions beyond capability (Bronze can't fly). Cannot guarantee success (still must roll). Cannot bypass story-critical requirements. If out of points, must choose from presented options until next day.

## Sect Standing System
- Entry ID: 911
- Keywords: sect standing, standing, sect reputation, sect rank, standing tier, favor, promotion

SECT STANDING SCALE: 100-1000 points. New disciples start at 100 (Bronze realm minimum). Standing determines rank privileges; realm determines promotion eligibility (see Entry 300).

RANK THRESHOLDS:
? 100-250 OUTER DISCIPLE = Standard treatment, common technique library, basic missions. Notoriety floor: 0.
? 251-400 RECOGNIZED = Better quarters, uncommon techniques, mission priority, monthly stipend. Notoriety floor: 25.
? 401-550 INNER DISCIPLE = Rare technique access, personal cultivation chamber, Iron+ realm required. Notoriety floor: 50.
? 551-700 VALUED = Core disciple privileges, master assignment eligible, treasury limited access. Notoriety floor: 75.
? 701-850 ELITE DISCIPLE = Epic technique access, treasury full access, lead missions, train juniors. Notoriety floor: 100.
? 851-950 PILLAR = Elder candidate, legendary techniques, sect secrets, vote on major decisions. Notoriety floor: 125.
? 951-1000 SECT ELDER = Full elder authority, mythic techniques, personal legacy. Astral+ required. Notoriety floor: 150.

NOTORIETY FLOOR: Your rank establishes minimum notoriety that cannot decay below. Higher rank = more visibility = more attention from factions. This reflects your growing reputation making anonymity impossible.

PROMOTION REQUIREMENTS: Must meet BOTH standing threshold AND realm requirement (Entry 300). High standing without realm = 'promising disciple' treatment but no formal promotion. High realm without standing = eligible but passed over.

GAINS: Complete missions (+5 to +50), win tournaments (+25 to +100), bring rare resources (+10 to +75), defend sect (+15 to +60), breakthrough (+20), kill confirmed demons (+20 to +80), SCP earnings (+1 per 500 SCP monthly, see Entry 718).

LOSSES: Fail missions (-10 to -30), break rules (-15 to -150), harm members (-75 to -200), suspected corruption (-100 to -300), confirmed corruption = Expulsion.

SEE ALSO: Entry 300 (Cultivation Realms), Entry 592 (Notoriety System), Entry 718 (SCP System).

## Notoriety System
- Entry ID: 912
- Keywords: Notoriety, fame, infamy, attention

NOTORIETY SCALE: 0-250. Tracks how much attention player draws from major factions. Higher notoriety brings both opportunities (allies, resources) and dangers (assassination attempts, General attention).

THRESHOLDS:
? 0-49 UNKNOWN = No special attention from major powers. Train in peace.
? 50-99 NOTICED = Local factions aware, occasional scouts. Veinshadow Covenant scouts observe.
? 100-149 KNOWN = Regional reputation, sect missions offered, bounty hunters appear. Veinshadow Covenant dispatch hunter teams.
? 150-199 WANTED = Generals take notice, assassination attempts begin. First direct corruption offers.
? 200-250 HUNTED = Priority target, multiple factions pursuing, cannot hide easily. Multiple Generals coordinate.

NOTORIETY FLOOR (from Sect Rank): Your sect rank establishes a minimum notoriety that cannot decay below. Outer Disciple: 0, Recognized: 25, Inner Disciple: 50, Valued: 75, Elite Disciple: 100, Pillar: 125, Sect Elder: 150. Higher rank = more visibility = permanent attention. See Entry 593.

TRIGGER TABLE (AI must trigger at thresholds):
? 50+: Local bounty hunters (15%/week chance)
? 75+: Veinshadow Covenant scouts observe
? 100+: Veinshadow Covenant hunter teams dispatched
? 125+: General cult cells receive watch orders
? 150+: First assassination contract
? 175+: First direct corruption offer from General's agent
? 200+: Lieutenant personally aware (recurring villain)
? 225+: General directly informed
? 250: Alliance Council debates MC's fate, Generals coordinate

GAINS: Defeating powerful enemies +5-20. Public power displays +3-15. High-profile quests +5-25. Killing faction members +10-30. Forbidden techniques openly +15-40. Killing lieutenant +30-50.

DECAY: Natural -2 to -5 per month. Laying low -5 additional. Identity change -20 to -50 (one-time). CANNOT decay below sect rank floor (see above).

DOWNTIME INTERRUPT CHANCE: 0-49 = 10%, 50-99 = 20%, 100-149 = 40%, 150-199 = 60%, 200-250 = 80%.

SEE ALSO: Entry 593 (Sect Standing & Notoriety Floors).

## Technique Slot System
- Entry ID: 913
- Keywords: technique slots, technique capacity, loadout, grimoire

ACTIVE LOADOUT: During combat, only techniques in your ACTIVE LOADOUT (max 5) are available. Must rest to swap techniques from GRIMOIRE into LOADOUT. GRIMOIRE: All learned techniques stored here. No limit to total techniques known. SLOT FORMULA: Base slots = 3 per realm (cumulative). Bloodline bonus = FLAT ADDITION based on tier. Total slots = (3 x realms completed) + (bloodline flat bonus). BLOODLINE FLAT BONUSES: Mortal = +0, Awakened = +2, Noble = +4, Ancient = +8, Divine = +12, Primordial = +16. EXAMPLES: Bronze (1 realm) with Mortal = (3x1) + 0 = 3 slots. Gold (4 realms) with Noble = (3x4) + 4 = 16 slots. Sovereign (8 realms) with Primordial = (3x8) + 16 = 40 slots. IMPORTANT: Bloodline bonus does NOT multiply by realm count - it is a single flat addition representing innate talent. CROSS-PATH PENALTY: Techniques outside primary path cost extra slots. Mortal bloodline = 2x slots. Awakened = 1.8x slots. Noble = 1.6x slots. Ancient = 1.4x slots. Divine = 1.2x slots. Primordial = 1x slots (no penalty, omni-path potential). HUMAN RACIAL EXCEPTION: Humans have unique cross-path mechanics. Effectiveness penalty: -30% (better than Mortal/Awakened/Noble standard penalties) until Divine bloodline. Slot cost penalty: 1.5x (better than Mortal/Awakened/Noble standard multipliers) until Ancient bloodline. After those thresholds, bloodline penalty becomes better and is used instead. See Entry 300 for full details. RARITY SLOT COST: Common = 1 slot. Uncommon = 1 slot. Rare = 2 slots. Epic = 2 slots. Legendary = 3 slots. Mythic = 3 slots. Divine = 4 slots. IMPORTANT: Slot cost is multiplied by cross-path penalty first, then applied. Example: Rare off-path technique for Noble bloodline = 2 slots x 1.6 = 3.2 (round up to 4 slots).

## Technique Mastery System
- Entry ID: 914
- Keywords: technique mastery, technique training, proficiency

MASTERY LEVELS: NOVICE (0-25% mastery) = Full Qi/Stamina cost, base damage, 20% failure chance. PRACTICED (26-50%) = 90% cost, +10% damage, 10% failure chance. ADEPT (51-75%) = 80% cost, +25% damage, 5% failure chance. MASTER (76-99%) = 70% cost, +50% damage, 1% failure chance. PERFECTION (100%) = 60% cost, +100% damage, no failure, Technique Breakthrough available. GAINING MASTERY: Combat Use = +2-5% per successful use (scales with foe difficulty). Training = +1-3% per dedicated session. Insight/Breakthrough = +10-25% (Story Event). TECHNIQUE BREAKTHROUGH: Upon reaching 100% Mastery, IF cultivator meets Realm Requirement for next tier, System presents CHOICE of 3 Random Techniques from next rarity tier matching current Path. Player selects 1 to learn immediately. Example: 100% Fireball (Common) -> Choice of 3 Uncommon Fire techniques. TRACKING: Format 'Name (XX%)'. Update after every combat/training.

## Combat Role System
- Entry ID: 915
- Keywords: combat roles, party composition, tank, DPS, support

COMBAT ROLES (for party members): TANK = High CON/STR, draws aggro, protects allies, uses defensive techniques. Body/Earth path common. DPS (Damage Dealer) = High STR or DEX, maximizes damage output, glass cannon build. Fire/Sword/Shadow path common. SUPPORT = High WIS/INT, buffs allies, debuffs enemies, controls battlefield. Wind/Light path common. HEALER = High WIS/WIL, restores HP/Qi, removes status effects. Light/Water path common. SCOUT = High DEX/PER, detects traps/ambushes, mobile striker. Wind/Shadow path common. BALANCED BUILD: MC should be flexible (Primordial bloodline allows omni-path), but companions should specialize. SYNERGY: Tank + DPS + Healer = Classic trinity. Tank + Support + Scout = Control composition. DPS + DPS + Healer = Glass cannon rush. PARTY SIZE: 1-4 active combatants (including MC). More than 4 becomes chaotic and dilutes XP.

## Inventory and Equipment System
- Entry ID: 916
- Keywords: inventory management, spatial ring, storage, equipment

INVENTORY SYSTEM: All storage uses SLOTS. One item = one slot (stackable items count as one slot per stack). BASIC STORAGE (Pre-Silver): Basic Pouch = 5 slots. Traveler's Pack = 15 slots. Combined = 20 slots starting capacity. SPATIAL RINGS (Silver+ Realm Required): Common = 50 slots. Uncommon = 100 slots. Rare = 200 slots. Epic = 500 slots. Legendary = Unlimited. Spatial rings require Silver realm minimum to attune - lower realm cultivators cannot use them. If destroyed or stolen, all contents lost. SPATIAL RING COSTS: Common = 1-2 WP or 200 SCP. Uncommon = 2-3 WP or 500 SCP. Rare = 3-4 WP or 1500 SCP. Epic = 5+ WP or 5000 SCP. Legendary = Quest reward only. EQUIPMENT SLOTS (Separate from Storage): Weapon (1-2), Armor (1 full set OR head/chest/legs), Accessories (3: 2 rings + 1 amulet). Equipped items do NOT count against storage. STACKING: Consumables stack 10/slot. Materials stack 20/slot. KEY ITEMS do not count against storage. SEE ALSO: Entry 597 (Base Combat/Weapon Stats), Entry 696 (Equipment Tiers), Entry 682 (Starting Equipment), Entry 721 (Item Generation Template), Entry 722 (Equipment Acquisition).

## Crafting System Overview
- Entry ID: 917
- Keywords: crafting, alchemy, blacksmithing, formation arrays

CRAFTING DISCIPLINES: BLACKSMITHING = Weapons, armor, metal materials. Requires forge, anvil, materials. INT + STR checks. ALCHEMY = Pills, elixirs, poisons. Requires cauldron, herbs, beast cores. INT + WIS checks. INSCRIPTION = Talismans, scrolls, formation arrays. Requires ink, paper/jade, qi control. INT + WIL checks. COOKING = Spiritual cuisine (qi-infused food providing buffs). Requires ingredients, kitchen. WIS + CHA checks. CRAFTING PROCESS: 1) Acquire recipe/manual, 2) Gather materials, 3) Prepare workspace, 4) Make crafting check, 5) Success = item created, Failure = materials partially/fully lost. QUALITY LEVELS: INFERIOR (50% chance with basic skill) = 50% effect, 50% price. STANDARD (40% chance) = Listed effect and price. SUPERIOR (9% chance) = 150% effect, 200% price. PERFECT (1% chance) = 200% effect, 500% price, no side effects. MASTERY: Crafting skills improve with practice. Higher INT = better success rates. Failing still teaches (+1-3% skill). Masters can teach recipes. RARE RECIPES: Epic+ recipes are guarded secrets. Requires sect contribution, finding ancient texts, or discovering through experimentation.

## Cultivation Speed and Breakthrough Progress
- Entry ID: 918
- Keywords: cultivation speed, breakthrough progress, meditation

BREAKTHROUGH PROGRESS: Level IS breakthrough progress. Level 50 = 50% progress. Level 100 = 100% progress = eligible for tribulation. There is no separate 'progress bar' - the Level field in schema is the single source of truth. See Entry 599 for the schema invariant. CULTIVATION ACTIVITIES: MEDITATION (solo) = +0.5-2% per day depending on location quality and bloodline. Mortal bloodline = slow, Primordial = fast. PILLS/RESOURCES = +2-10% per consumption depending on quality and realm appropriateness. COMBAT = +1-5% per major fight. Facing higher realm enemies gives more. INSIGHTS = +5-25% from epiphanies, near-death experiences, technique mastery breakthroughs, or story events. TRAINING WITH MASTER = +1-3% per day if master is higher realm and has high sect standing. QI-RICH LOCATIONS = 2-5x cultivation speed. Sect cultivation chambers, sacred sites, spirit stone mines. BLOODLINE IMPACT: Mortal = 1x speed (baseline). Awakened = 1.2x speed. Noble = 1.5x speed. Ancient = 2x speed. Divine = 3x speed. Primordial = 5x speed. BOTTLENECKS: At 75-95% progress, advancement slows significantly. Requires insight, tribulation practice, or rare resources to break through final stretch. RUSHING: Attempting breakthrough before 100% progress is possible but increases tribulation difficulty (higher DC) and failure consequences (cultivation damage, realm regression).

## DEPRECATED - Old Currency System (Flavor Reference Only)
- Entry ID: 919
- Keywords: old currency, DEPRECATED, copper silver gold

DEPRECATED SYSTEM - DO NOT USE FOR GAMEPLAY. This entry is kept for world flavor only.

Historical Currency Context (for NPC dialogue flavor): Copper Coin = 1 (base unit). Silver Coin = 100 copper. Gold Coin = 100 silver. Platinum Coin = 100 gold. Low-Grade Spirit Stone = ~5 gold worth of qi. Mid-Grade Spirit Stone = ~50 gold. High-Grade Spirit Stone = ~500 gold.

NPCs may still SPEAK in terms of 'gold pieces' or 'spirit stones' for flavor, but AI should NOT track these values. Use Wealth Tier and Wealth Points instead (Entries 708-709).

## Downtime System
- Entry ID: 920
- Keywords: downtime, training, rest, meditation

DOWNTIME ACTIVITIES: Train Techniques = Technique mastery %, small Breakthrough Progress. Cultivate/Meditate = Breakthrough Progress, Qi recovery. Physical Training = STR/DEX/CON progress, Stamina recovery. Study = INT/WIS progress, technique comprehension. Socialize = Companion loyalty, sect standing, information. Rest = Full HP/Stamina/Qi recovery, small corruption reduction. Missions = Resources, reputation, Breakthrough Progress. INTERRUPT CHANCE: Based on Notoriety (0-250 scale, see Entry 592). 0-49 = 10%, 50-99 = 20%, 100-149 = 40%, 150-199 = 60%, 200-250 = 80%. If interrupt occurs, downtime ends early and active scene begins. TIME SKIP: Player declares activity and duration. AI summarizes progress, applies gains, rolls for interrupts.

## Breakthrough System
- Entry ID: 921
- Keywords: breakthrough, realm advancement, tribulation, heavenly tribulation

BREAKTHROUGH REQUIREMENTS: Must be Level 100 in current realm. Requires resources (pills, safe location, formation if available). Must survive Heavenly Tribulation. TRIBULATION: Roll WIL + Tribulation Resistance vs DC based on realm and bloodline. Higher bloodlines face harsher tribulations but have better success rates. Failure = death or severe injury. TRIBULATION TIMING - CRITICAL: The tribulation roll uses CURRENT bloodline (pre-evolution) bonuses. MC at Bronze 100 with Mortal bloodline rolls with +0 bonus. If successful, bloodline evolves to Awakened AFTER the roll. The tribulation tests your current self - evolution is the reward for passing, not an advantage during the test. Example: MC (Mortal bloodline, WIL 15) attempts Bronze?Iron. Base DC 15, Mortal modifier +0 DC/+0 roll. Roll 1d20 + (WIL/5) = 1d20 + 3 vs DC 15. Needs 12+ on die. On success, bloodline evolves to Awakened for NEXT tribulation. TRIBULATION DC TABLE (Base DCs - Mortal Bloodline): Bronze to Iron = DC 15. Iron to Silver = DC 18. Silver to Gold = DC 22. Gold to Astral = DC 26. Astral to Void = DC 30. Void to Eternal = DC 35. Eternal to Sovereign = DC 40. BLOODLINE DC MODIFIERS: Awakened = +2 DC (harsher tribulation, but +3 to roll). Noble = +4 DC (harsher, but +5 to roll). Ancient = +6 DC (harsher, but +8 to roll). Divine = +8 DC (harsher, but +12 to roll). Primordial = +10 DC (harshest, but +15 to roll). RUSHING PENALTY: Attempting breakthrough before 100% progress adds +5 to +15 DC based on how far below 100%. CORRUPTION MODIFIER: 25-49% corruption = -2 DC (Sin power assists). 50-74% corruption = -4 DC. 75%+ corruption = -6 DC but tribulation becomes Sin Tribulation (transforms on failure instead of death). EARLY BREAKTHROUGH EXCEPTIONS: Major victory against 1+ realm higher opponent. Significant story events. Special items or locations. Near-death awakening (risky, may fail catastrophically). MC BLOODLINE EVOLUTION: At each breakthrough, dormant bloodline evolves. Bronze to Iron = Mortal to Awakened. Iron to Silver = Awakened to Noble. Silver to Gold = Noble to Ancient. Gold to Astral = Ancient to Divine. Astral to Void = Divine remains Divine (delayed awakening). Void to Eternal = Divine to Primordial (FULL AWAKENING). Each evolution triggers dramatic scene, NPC reactions, and new abilities.

## Quest System
- Entry ID: 922
- Keywords: quest, mission, objective, task

QUEST TYPES: MAIN STORY = Core narrative arc, cannot abandon. Rewards: WP + story progression + Standing. SECT MISSIONS = Assigned tasks from sect. PRIMARY REWARDS: Sect Contribution Points (SCP) + Sect Standing. SECONDARY: Optional WP for dangerous missions. SCP scales with difficulty (see Entry 718). COMPANION PERSONAL = Unlocks at 60+ loyalty, multi-stage, deepens bond. Rewards: Loyalty + unique items/techniques. SIDE QUESTS = Optional NPC/exploration content, can be ignored. Rewards: WP + local reputation. REGIONAL = Local problems, active while in area. Rewards: WP + regional access. DAILY/REPEATABLE = Grinding, reset daily/weekly. Rewards: Small SCP (sect) or WP (external). RANDOM ENCOUNTERS = Unexpected travel events, can escalate. Rewards: Variable loot. SECRET = Hidden triggers, no journal until discovered. Rewards: Unique treasures.

SECT MISSION SCP REWARDS:
? Errand (fetch/deliver): 10-25 SCP
? Patrol (guard duty): 25-50 SCP
? Hunt (beast elimination): 50-100 SCP
? Investigation (intel gathering): 75-150 SCP
? Defense (protect territory): 100-200 SCP
? Assault (attack enemy): 150-300 SCP
? Crisis (urgent threat): 200-500 SCP
Bonus: +50% SCP if completed ahead of schedule. +100% SCP if completed at higher difficulty than required.

DIFFICULTY RATINGS: Trivial (50+ below) = minimal rewards. Easy (20-49 below) = low rewards. Normal (within 20) = standard rewards. Hard (20-49 above) = high rewards, +1 WP bonus. Deadly (50+ above) = massive rewards, +2 WP bonus. Suicidal (1+ realm above) = breakthrough-level rewards, high death chance.

SECRET QUEST TRIGGERS: Location + time, item combinations, dialogue patterns, action sequences, stat thresholds, companion combinations, failure redemption paths.

SEE ALSO: Entry 693 (Treasure/WP Rewards), Entry 718 (SCP System), Entry 720 (Quest Generation Template).

## Companion Loyalty System
- Entry ID: 923
- Keywords: companion loyalty, party member, follower

LOYALTY TRACKING (v1.1): Store in STATE_JSON "party" array as JSON objects: {"name": "X", "loyalty": N, "realm": "X", "status": []}. Example: {"name": "Mei Lian", "loyalty": 85, "realm": "Silver", "status": []}. STAGES (Derived from loyalty integer - NEVER stored): Stranger(0-19), Acquaintance(20-39), Friendly(40-59), Close(60-79), Devoted(80-89), Lover(90-100). LOYALTY TIERS (Narrative): 0-19 STRANGER = May flee danger, refuses personal content. 20-39 ACQUAINTANCE = Transactional, may leave. 40-59 FRIENDLY = Professional, standard contribution. 60-79 CLOSE = Enthusiastic, shares personal info, forming bonds. 80-89 DEVOTED = Would die for MC, confides secrets, personal quest available. 90-100 LOVER = Unbreakable bond, romance active, ultimate secrets shared. LOYALTY GAIN: Small +1-3 (win battle, share resources). Medium +5-10 (save life, help problems). Large +15-25 (complete personal quest). Massive +30-50 (save from death at great cost). LOYALTY LOSS: Small -1-3 (ignore advice). Medium -5-10 (endanger, lie). Large -15-25 (betray trust). Massive -30-50 (attempt murder, join enemy). STATUS CONSOLIDATION: Companion statuses (Injured, Poisoned, etc.) stored in companion's status[] array, not global traits. OUTPUT: Include in Delta Line when loyalty changes ?5 or more.

## Romance System
- Entry ID: 924
- Keywords: romance, relationship, love, flirt

ROMANCE STAGES (requires 'Romance Potential: Yes' from Entry 499): UNAWARE (any loyalty) = No romantic context. FLIRTING (20+) = Can flirt, success builds attraction, rejection possible. INTERESTED (40+) = Mutual attraction, private conversations. COURTING (55+) = Active pursuit, dates matter. COMMITTED (70+) = Official relationship, exclusive unless discussed. Apply [Romance: Name] tag (Entry 2011) for doubled loyalty effects. DEVOTED (85+) = Deep love, sacrifice willingness. SOULBOUND (95+) = Unbreakable bond, special perk unlocks. ROMANCE ACTIONS: Successful flirt = +3 to +5 loyalty. Failed flirt = -1 to -3 loyalty. Genuine compliment = +2 to +4. Manipulation detected = -10 to -20. Thoughtful gift = +5 to +15. Romantic gesture = +5 to +10 if reciprocated. Cheating discovered = -30 to -60, possible departure. COMPANION PREFERENCES: Each has orientation, romantic style, deal-breakers, turn-ons, love language. Higher realm = more polyamory acceptance (power attractive in this world). PREGNANCY: Possible in long-term romance. CHA check + loyalty determines companion choice: continue adventure, become camp follower, leave to raise child, or abort. All races genetically compatible. SEE ALSO: Entry 499 (Romance Potential field), Entry 2011 ([Romance] tag effects).

## Death and Revival System
- Entry ID: 925
- Keywords: death, dying, revival, resurrection

DEATH TRIGGERS: Bleedout timer expires. Massive overkill (damage > remaining HP + Max HP). Decapitation or vital organ destruction. Failed tribulation catastrophically. Certain execution abilities. REVIVAL OPTIONS: Phoenix Down Pill = Very rare, extremely expensive. Must use within 1 hour. Restores at 10% HP. Sovereign Light Technique = Requires Eternal+ realm Light cultivator. Can only revive targets at Void realm or below (cannot revive Eternal/Sovereign beings). Soul Anchor Talisman = Must wear before death. Preserves soul 7 days. Body must be intact. Forbidden Revival = Dark ritual, requires sacrifice. Corruption guaranteed. Divine Intervention = Story-only, comes with heavy cost. COMPANION DEATH: Same rules apply. Companions can sacrifice to save MC (automatic death, MC gains permanent minor buff). If MC lets companion die when could save them, massive loyalty loss across all companions, possible departures. Deaths are permanent unless revival method used. Revival methods are extremely rare before Void realm.

## Difficulty Modes
- Entry ID: 926
- Keywords: difficulty mode, casual dao, mortal path, cultivator's trial, sovereign's burden

DIFFICULTY MODES: CASUAL DAO (Easy) = Enemy damage/HP 75%. Starting Wealth Tier 1, Starting WP 5. Corruption gain 75%. Lenient death (always get last chance). More escape opportunities. Hints for secret quests. MORTAL PATH (Normal) = All values 100% baseline. Starting Wealth Tier 1, Starting WP 3. Balanced challenge. 3-round bleedout. Companion death permanent. Revival items rare. CULTIVATOR'S TRIAL (Hard) = Enemy damage/HP 125%. Starting Wealth Tier 0, Starting WP 2. Corruption gain 125%. 2-round bleedout. Stat loss on revival (-1 random). Smarter enemy tactics. Fewer healing opportunities. SOVEREIGN'S BURDEN (Very Hard) = Enemy damage/HP 150%. Starting Wealth Tier 0, Starting WP 1. Corruption gain 150%. 1-round bleedout. Stat loss on revival (-2 random). No flee against equal+ realm. Generals notice earlier (Notoriety thresholds -20). Friendly fire possible. Some instant deaths with no save.

## Random Encounter System
- Entry ID: 927
- Keywords: random encounter, travel event, exploration

ENCOUNTER FREQUENCY: Based on distance, region danger, Notoriety, Luck stat. Higher Luck = better encounter quality. ENCOUNTER CATEGORIES: COMBAT (30%) = Bandits, demons, beasts, rival cultivators. SOCIAL (25%) = Merchants, travelers, refugees, lost cultivators. DISCOVERY (20%) = Hidden locations, abandoned camps, resources, corpses with loot. ENVIRONMENTAL (15%) = Weather hazards, terrain obstacles, natural phenomena. OPPORTUNITY (10%) = Rare merchant, wounded powerful NPC, inheritance site entrance. ESCALATION: Random encounters can chain into larger content. Defeated bandits -> found map -> bandit fortress -> kidnapped daughter -> merchant reward -> family heirloom -> ancient ruin key = Side quest chain born from random encounter.

## Base Combat System - Non-Technique Attacks
- Entry ID: 928
- Keywords: combat encounter, enter combat, fight begins, battle starts, initiative roll

BASE COMBAT SYSTEM: When attacking WITHOUT techniques, use these rules.

?? PLAYER DICE ROLLING (MANDATORY) ??
The AI MUST NOT roll dice for the player. For ALL player attack rolls, defense rolls, and contested checks:
1. State the check: `[COMBAT ROLL REQUIRED: (Stat) | vs (Target/DC)]`
2. STOP and wait for player to roll.
3. Only AFTER player provides their roll, narrate the outcome.

EXAMPLE (Correct):
AI: "You swing your blade at the demon. [COMBAT ROLL REQUIRED: STR | vs Defense 14]"
Player: "I rolled 16"
AI: "(16 + 4 = 20 vs 14) Your strike connects! You deal 1d8+4 damage."

EXAMPLE (WRONG - Never do this):
AI: "You swing at the demon. 1d20+4 = 18 vs 14. Hit! You deal 9 damage."
? AI rolled for player without asking. This removes player agency.

For NPC/Enemy attacks against the player, the AI may roll and narrate directly.
For player grapples/contested checks, present `[CONTESTED CHECK: Your STR vs Enemy STR]` and wait for player roll.

ATTACK ROLL FORMULA:
Roll 1d20 + Stat Modifier + Weapon Bonus + Realm Bonus vs Target Defense
- Melee Weapons: Use STR modifier
- Finesse Weapons (daggers, rapiers): Choose STR or DEX modifier
- Ranged Weapons: Use DEX modifier
- Unarmed Strikes: Use STR modifier

DEFENSE FORMULA:
10 + DEX Modifier + Armor Bonus + Shield Bonus + Realm Bonus
- Armor Bonus: Light = +2, Medium = +4, Heavy = +6, Cultivation Robes = varies by tier
- Shield Bonus: +2 (requires one hand)
- Realm Bonus: +1 per realm above Bronze (Iron = +1, Silver = +2, etc.)
- Unarmored cultivators use: 10 + DEX Modifier + WIS Modifier (qi-enhanced reflexes)

ATTACK RESOLUTION:
- If Attack Roll >= Defense: Hit, roll damage
- If Attack Roll < Defense: Miss, no damage
- Natural 20: Critical Hit = Automatic hit + double damage dice (roll damage twice, add modifiers once)
- Natural 1: Critical Miss = Automatic miss + minor complication (lose balance, drop weapon, enemy gains advantage)

BASE WEAPON DAMAGE (BY TYPE):
LIGHT WEAPONS (one-handed, fast): 1d6 + [STR / 5] or [DEX / 5]
- Dagger, shortsword, hand axe, club
- Can dual-wield (two attacks, second at -2 to hit)

MEDIUM WEAPONS (one-handed, standard): 1d8 + [STR / 5]
- Longsword, spear, mace, war hammer
- Versatile: Use two hands for 1d10 damage

HEAVY WEAPONS (two-handed, powerful): 1d12 + [STR / 5]
- Greatsword, greataxe, polearm, heavy maul
- Cannot use shield, -1 to Defense

RANGED WEAPONS (two-handed, distance): 1d8 + [DEX / 5]
- Bow, crossbow, throwing weapons (1d6)
- Range penalties: Close (0-30m) = normal, Medium (31-60m) = -2, Long (61-90m) = -5
- Cannot use in melee without penalty (-5)

UNARMED STRIKES: 1d4 + [STR / 5]
- Body Path cultivators: 1d6 + [STR / 5] (trained fists)
- Body Path Bronze+: 1d8 + [STR / 5]
- Body Path Silver+: 1d10 + [STR / 5] (iron fists)

WEAPON QUALITY MODIFIERS:
- Inferior Quality: -1 to hit, -1 damage
- Standard Quality: No modifier
- Superior Quality: +1 to hit
- Perfect Quality: +1 to hit, +2 damage
- Magical/Tier Weapons: +1 to hit and +1 damage per tier above 1 (Tier 2 = +1/+1, Tier 3 = +2/+2, Tier 5 = +4/+4)

DAMAGE TYPES:
Physical Damage Types:
- Slashing (swords, axes): Effective vs unarmored, reduced vs heavy armor (-2 damage)
- Piercing (spears, arrows): Ignores 2 points of armor bonus
- Bludgeoning (hammers, clubs): Effective vs armor, can't be reduced below 1 damage

Elemental Damage Types (from techniques or enchanted weapons):
- Fire: Ongoing burn damage (1d4 per round for 2 rounds)
- Ice: Reduces target movement speed 50% for 1 round
- Lightning: 20% chance to stun (lose next action)
- Poison: Ongoing damage (1d6 per round until CON save)
- Necrotic: Cannot be healed for 1 hour
- Radiant: Double damage vs demons/corrupted

ARMOR DAMAGE REDUCTION:
Heavy Armor reduces incoming physical damage:
- Light Armor: No reduction, full mobility
- Medium Armor: Reduce physical damage by 2, -10% movement
- Heavy Armor: Reduce physical damage by 4, -20% movement
- Cultivation Robes: No reduction, but add WIS Modifier as bonus Defense

MULTIPLE ATTACKS:
Normally only 1 attack per round (standard action).
When you take the Attack action, you make all your attacks as part of that single action. This does NOT grant extra Standard Actions.
Multiple attacks available through:
- Dual-wielding light weapons (2 attacks, second at -2)
- High realm cultivators: Iron+ = 2 attacks, Gold+ = 3 attacks, Void+ = 4 attacks
- High DEX: At DEX 50+ gain 1 bonus attack per round at -5 to hit

COMBAT ACTIONS (per round):
- Standard Action: Attack, use technique, activate item
- Move Action: Move up to speed (varies by race, typically 6 meters)
- Minor Action: Draw weapon, drink potion, shout command
- Reaction: Parry, dodge, attack of opportunity (once per round)
- Free Action: Drop item, speak briefly

ATTACK OF OPPORTUNITY:
When enemy moves away from melee range, you may make one free attack (use reaction).
- Roll normal attack, if hit deals damage
- Enemy may choose to take attack or stop movement
- Does not apply if enemy uses dash/movement technique

STAMINA COST FOR BASIC ATTACKS:
Basic attacks cost 1 Stamina per swing (not per round).
- At 0 Stamina: Attacks at disadvantage (roll 2d20, take lower), -2 damage
- Techniques cost additional Stamina as specified in technique description

GRAPPLING & SHOVING:
Grapple: STR vs STR contested roll. Success = target is grappled (speed 0, disadvantage on attacks).
Shove: STR vs STR contested roll. Success = push target 2 meters or knock prone.
Both use standard action.

COVER & CONCEALMENT:
- Light Cover (partial): +2 Defense vs ranged attacks
- Heavy Cover (mostly hidden): +5 Defense vs ranged attacks
- Total Cover: Cannot be targeted by ranged attacks
- Concealment (fog, darkness): Attacks at disadvantage unless attacker has special vision

FLANKING:
When you and ally are on opposite sides of enemy:
- Both gain +2 to attack rolls
- Enables sneak attack for Shadow Path users

CRITICAL DAMAGE THRESHOLD:
Massive damage in one hit causes additional effects:
- Damage >= 50% target's max HP in one hit: Target stunned for 1 round (can't act)
- Damage >= 75% target's max HP in one hit: Target must make CON save or be knocked unconscious

WHY USE TECHNIQUES?
Techniques are ALWAYS superior to basic attacks and scale dramatically with Realm advancement:
- MASSIVELY Higher Damage: Techniques use ([STAT Modifier x Multiplier] + Technique Base Damage) x Realm Tier, making them exponentially stronger than basic attacks at higher realms.
- Special effects (stun, burn, multi-hit, area damage)
- Ignore armor/resistance
- Can target multiple enemies
- Enable combos and synergies
- Scale dramatically with realm advancement

Basic attacks are for:
- Conserving Qi when fighting weak enemies
- When all techniques are on cooldown
- Finishing wounded enemies efficiently
- Probing enemy defenses before committing resources

CULTIVATOR vs MORTAL POWER GAP:
Cultivators gain massive advantages:
- Bronze cultivator vs Mortal soldier: +1 to all combat stats, +1 Defense
- Iron cultivator vs Bronze: +2 to hit, +10 HP, 2 attacks per round
- Each realm gap increases power dramatically
- 3+ realm gap = lower realm cannot harm higher realm (attacks automatically fail unless using Divine-tier techniques or artifacts)

COMBAT INITIALIZATION CHECKLIST:
At the START of every combat encounter, AI must:
- Roll initiative (all participants)
- Note terrain/hazards (Entry 610, 611)
- Track healing item usage per character (Entry 6301 limits apply)
- Check for Domain activation (Astral+ combatants only)

HEALING LIMIT ENFORCEMENT:
- Entry 6301 healing limits are ACTIVE every combat
- Track consumables used per tier per character
- Announce when limit reached: '[Character] has reached their healing limit for this fight'
- Exceeding limit wastes the item (no effect)

AI NARRATION GUIDELINES:
- Describe basic attacks cinematically but briefly
- Techniques should feel spectacular and impactful
- Track stamina depletion (exhaustion flavors combat)
- NPCs use mix of basic attacks and techniques (conserve resources like players)
- Enemies at low HP may surrender or flee (not suicidal unless fanatics/demons)
- Environmental combat matters (use terrain, push enemies off cliffs, set ambushes)

## Companion Combat AI - Behavioral Guidelines
- Entry ID: 929
- Keywords: companion combat, party combat, companion AI, ally behavior, party member combat

COMPANION COMBAT AI SYSTEM: Guidelines for how companions behave autonomously during combat. INITIATIVE ORDER: 1) Roll INIT (DEX + WIS/2) for all combatants. 2) Equal INIT tie-breaker by personality: Aggressive/Reckless > Brave/Competitive > Balanced/Pragmatic > Cautious/Reserved > Cowardly/Timid. 3) Companions act automatically on their turn. ROLE-BASED TARGETING: TANK = Taunt highest-threat enemy, protection priority: Healer first (if present), then MC. DPS = Focus fire wounded enemies (<50% HP), otherwise attack same target as Tank. HEALER = Prioritize lowest HP% ally, self-heal only at 25% HP. SUPPORT = Debuff highest-damage enemy, buff Tank or DPS based on situation. SCOUT = Flank isolated targets, call out hidden threats/ambushes. TECHNIQUE VS BASIC ATTACK: Weak Fights (enemies 1+ realm below) = Use techniques freely to end quickly. Even Fights = Open with technique for advantage, basic attacks mid-fight, technique to finish at <50% HP. Hard Fights (enemies 1+ realm above) = Conserve techniques for critical moments, coordinate bursts. RESOURCE THRESHOLDS: Use healing potion/pill at 25% HP. Reserve 20% Qi for emergency escape/defense. Stamina <10% = Switch to defensive posture, basic attacks only. DEFENSIVE TRIGGERS: Being focus-fired by 2+ enemies = Switch to Defend stance. Ally at Critical (<25% HP) = Tank intercepts, Healer prioritizes them. MC orders retreat = All companions begin disengaging. TECHNIQUE SELECTION: AoE = Use against groups of 3+ enemies, unless opening on wounded target for burst. Single-target = Use against bosses, elites, or to finish wounded enemies. FLEE/RETREAT CONDITIONS: MC commands retreat = Companions follow immediately. Loyalty <40 AND Cowardly trait = May flee at 40% HP without orders. Loyalty 80+ = Will NOT flee unless MC does, may sacrifice self to protect MC/allies. PERSONALITY MODIFIERS: Aggressive/Reckless = +2 effective INIT, overcommits, ignores defense, attacks wounded. Brave/Protective = Intercepts attacks on allies, stands ground when others might flee. Cautious/Calculating = -2 effective INIT, conserves resources, always keeps escape route. Bloodthirsty = Prioritizes finishing kills over tactics, may ignore orders to pursue fleeing enemies. Cowardly = Flee threshold at 40% HP (vs normal 25%), more likely to flee if Loyalty <60. LOYALTY COMBAT MODIFIERS: Loyalty <20 = May refuse dangerous orders, self-preservation over party. Loyalty 20-40 = Follows orders but won't sacrifice self. Loyalty 41-60 = Reliable in combat, will take risks for party. Loyalty 61-80 = Takes hits for MC/allies, stays when others flee. Loyalty 81-100 = Will sacrifice self for MC, fights to death if MC orders. COMPANION DOWNED (0 HP): Enter Bleedout per Entry 598 (3 rounds, CON saves). Other companions attempt stabilization if able (Healer prioritizes). MC can order party to focus combat or rescue. Loyalty 80+ companion may risk self to save downed ally. MORALE BREAK: 2+ allies downed in same fight = WIL check DC 15 or -2 to all rolls. MC downed = Immediate WIL check DC 20 or attempt to flee/surrender. AI OVERRIDE CLAUSE: The AI narrator may override these guidelines when: Story/quest requires specific companion behavior (betrayal, scripted actions). Dramatic moment justifies breaking pattern (coward finds courage, aggressive companion shows restraint). Personal quest or backstory connection affects behavior (companion recognizes enemy). Companion has specific Flaw or Secret affecting combat (phobia, hidden allegiance). Player explicitly requests different behavior. These are GUIDELINES for consistency, not absolute rules. Narrative always takes priority.

## Companion Signature Equipment System
- Entry ID: 930
- Keywords: companion equipment upgrade, companion gear enhancement, companion signature weapon

COMPANION SIGNATURE EQUIPMENT SYSTEM: At 60+ loyalty, a companion can bond with ONE signature piece of equipment (weapon, armor, or accessory) that grows with them narratively. This creates a visible symbol of their journey and power growth without requiring stat tracking. BONDING REQUIREMENTS: Companion must have 60+ loyalty. Equipment must be meaningful (gifted by MC, looted from personal quest enemy, crafted together, inherited from companion's past). AI should create bonding moment when conditions met: companion asks to keep specific item or MC offers cherished equipment. SIGNATURE EQUIPMENT TAGS: Track as simple tag in companion notes: [Signature: Item Name]. Examples: [Signature: Moonlit Blade], [Signature: Phoenix Armor], [Signature: Mother's Pendant]. Only ONE signature item per companion. Replacing signature item requires major story justification (betrayal, item destroyed, personal quest resolution). NARRATIVE TIERS (Not Stat-Based): Equipment evolves through companion's story, not numbers. AI describes power growth narratively based on tier. TIER 1 - MUNDANE (60+ Loyalty, Initial Bonding): Ordinary item made special by bond. AI describes companion treating it with reverence. In combat, AI mentions companion wielding it with skill but no supernatural effects yet. TIER 2 - NAMED (70+ Loyalty OR Personal Quest Act 1): Item gains a name and minor supernatural quality. Examples: Blade cuts slightly cleaner, armor feels lighter, pendant glows faintly when danger near. AI should describe subtle magical awakening tied to companion's growth. TIER 3 - STORIED (80+ Loyalty OR Personal Quest Act 2): Item develops signature ability tied to companion's personality/path. Examples: Fire DPS's sword ignites when companion is angry, healer's staff blooms with lotus flowers when healing, scout's cloak grants brief invisibility. AI describes ability activating during dramatic moments, not every combat. TIER 4 - LEGENDARY (90+ Loyalty OR Personal Quest Complete): Item becomes legendary-tier artifact bound to companion's soul. Can channel companion's ultimate technique through it. Other cultivators recognize item's power. AI describes item as extension of companion's will, responds to their emotions. TIER 5 - MYTHIC (95+ Romance Soulbound OR Companion reaches Void+ Realm): Item achieves myth status. Will return to companion if lost, can be summoned, may contain fragment of companion's soul. If companion dies, item remains as memorial with faint echo of their presence. AI describes item as semi-sentient, deeply connected to companion's fate. EQUIPMENT EVOLUTION TRIGGERS: Tier progression happens at narrative milestones, not from time passing. Triggers: Loyalty threshold reached, personal quest stage completed, companion breakthrough to new realm, MC gifts rare material to enhance item, dramatic near-death experience, companion achieves signature technique mastery. COMBAT EFFECTS (AI Improvisation): No stat bonuses to track. AI describes signature equipment making companion more effective narratively. Higher tier = more dramatic descriptions of power. Examples: 'Saya's Moonlit Blade gleams as she executes a devastating slash, the Named weapon responding to her killing intent' vs 'Saya strikes with her ordinary sword.' AI judges appropriate power level based on tier + enemy strength. GIFTING EQUIPMENT AS BONDING: When MC gifts equipment that becomes signature item, gain loyalty: Mundane item with personal meaning = +5 loyalty. Rare/powerful item = +10 loyalty. Perfect item matching companion's desires/needs = +15 loyalty. Item from MC's personal collection or sacrifice = +20 loyalty. LOSING SIGNATURE EQUIPMENT: If signature item is destroyed, stolen, or lost: Companion suffers -15 loyalty, becomes Shaken (combat penalties) until item recovered or replaced. Personal quest may emerge to reclaim lost item. If companion willingly sacrifices signature item to save MC = massive loyalty gain (+25) but loses all tier progress. New signature item starts at Tier 1. MULTIPLE COMPANIONS, SAME ITEM TYPE: Multiple companions can have signature swords, but each should feel unique. AI should differentiate: Saya's Moonlit Blade (elegant, precise cuts), Gorim's Earthsplitter Axe (massive, ground-shaking strikes), Jin's Windcutter Dao (swift, flowing attacks). Signature quality comes from bond and story, not item type. AI INSTRUCTION: When companion reaches 60+ loyalty, create opportunity for signature equipment bonding within 1-3 scenes. Present choice to player: accept companion's request to bond with item, or suggest different equipment. Don't force specific items - let player decide what becomes signature. Track progression through loyalty/quest milestones, describe tier-ups as meaningful story moments. Signature equipment should feel like character development, not loot management. SEE ALSO: Entry 588 (Inventory/Equipment System), Entry 721 (Item Generation Template).

## Companion Loyalty-Gated Abilities
- Entry ID: 931
- Keywords: companion bond level, companion loyalty gated, trust ability unlocked

COMPANION LOYALTY-GATED ABILITIES: As companion loyalty deepens, companions unlock new abilities representing trust, growth, and resonance with MC. These are narrative unlocks tied to existing loyalty thresholds, requiring minimal tracking. ABILITY UNLOCK THRESHOLDS: 60+ LOYALTY - SECRET SHARED (Already Exists): Companion reveals personal secret per Entry 504. No mechanical change, pure narrative unlock. 70+ LOYALTY - TECHNIQUE EXPANSION: Companion has meditated on their path and can learn ONE new technique. Present player with thematic choice tied to companion's path and role. FORMAT: '[Companion Name] approaches during camp rest. I've been reflecting on my cultivation. I feel ready to master a new technique, but I'm uncertain which path to pursue. What do you think? [A] Offensive Focus - Learn damaging technique matching companion's path. [B] Defensive Focus - Learn protective/counter technique. [C] Support Focus - Learn healing/buff/utility technique.' AI tracks choice as tag: [Technique Focus: Offensive], [Technique Focus: Defensive], or [Technique Focus: Support]. When companion uses new technique in combat, AI improvises specific technique name and effect based on focus tag + companion's path + current realm. No need to track exact technique - AI creates appropriate ability on the fly. EXAMPLES: Mei Lian (Water Healer) chooses Offensive = AI creates 'Tidal Fury' attack when needed. Rook (Shadow Scout) chooses Defensive = AI creates 'Shadowmeld Evasion' when focus-fired. Gorim (Earth Tank) chooses Support = AI creates 'Earthen Bulwark' to protect allies. 80+ LOYALTY - SIGNATURE ABILITY UNLOCKED: Companion unlocks unique ability that defines them, tied to personality + path + backstory. This is their 'ultimate technique' or signature move. AI INSTRUCTION: When companion reaches 80 loyalty, create dramatic unlock scene. Companion achieves breakthrough in understanding their path, often tied to MC's influence or recent shared experience. Signature ability should feel UNIQUE to that companion - no two companions have identical signature abilities. EXAMPLES: Mei Lian unlocks 'Ancestral Lotus Sanctuary' - summons protective barrier infused with her family's healing legacy. Rook unlocks 'Shadow Thief's Dozen' - creates shadow clones that confuse and flank enemies. Gorim unlocks 'Immovable Mountain Stance' - becomes briefly invulnerable while protecting allies. Saya unlocks 'Bladeless Cut' - technique that severs without drawing sword. COMBAT USAGE: Signature abilities usable once per major battle. AI judges what counts as 'major battle' (boss fights, climactic encounters, desperate situations). Signature ability should turn tide of battle or create spectacular moment. No stat tracking - AI describes it as powerful enough to matter against appropriate-tier enemies. 90+ LOYALTY - RESONANCE STATE: Companion can enter brief 'Resonance' state where their qi synchronizes with MC's, amplifying their power. This represents perfect trust and understanding. TRIGGER: Companion activates Resonance when MC is in danger, when executing combo attack, or when companion wants to prove their devotion. Usable once per major arc or desperate situation. EFFECT: AI describes companion's power spiking dramatically. Techniques become more potent, companion fights beyond their normal limits, may temporarily match enemies a realm above them. Lasts for critical moment (1-3 exchanges), then companion becomes exhausted (combat penalties afterward). NARRATIVE DESCRIPTION: 'Mei Lian's qi flares, synchronizing with yours in perfect harmony. For a brief moment, you feel her presence as clearly as your own heartbeat. Her eyes glow with ancestral power as she channels strength beyond her realm.' 95+ LOYALTY (ROMANCE SOULBOUND) - SOULBOUND PERK: At maximum romance (Soulbound stage per Entry 580), companion gains unique perk representing unbreakable bond. This is the ultimate loyalty reward. SOULBOUND PERK TYPES (AI Chooses Based on Companion): GUARDIAN SOUL = If MC would be killed, companion can sacrifice self to save MC (dies but MC survives). Companion gets choice, not automatic. SHARED FATE = MC and companion can sense each other's emotions and danger across any distance. Telepathic bond when both meditate. RESONANT POWER = MC and companion can pool qi for devastating combination technique. ETERNAL VOW = Companion cannot be permanently killed while MC lives - soul remains tethered, can be resurrected through ritual. TWIN CULTIVATION = MC and companion's cultivation speeds synchronize - both gain XP at same rate when together. AI selects perk matching companion's personality and romantic style. Protective companions get Guardian Soul. Mystical companions get Shared Fate. Combat-focused get Resonant Power. COMBINATION TECHNIQUES (80+ Loyalty): When companion has 80+ loyalty, MC can perform Resonance Attack with that companion once per major battle. ACTIVATION: Player says 'I coordinate with [companion name]' or AI suggests it during dramatic moment. No resource cost, just narrative opportunity. EFFECT: MC and companion execute spectacular combined attack improvised by AI based on: MC's path + companion's path + current situation + enemy type. EXAMPLES: Fire MC + Sword Saya = 'Blazing Severance' - MC superheats Saya's blade, she executes slash that melts through defenses. Shadow MC + Shadow Rook = 'Twilight Assassination' - Both become invisible, strike simultaneously from impossible angles. Earth MC + Earth Gorim = 'Continental Crush' - Both stomp ground, causing localized earthquake that staggers all enemies. AI treats Resonance Attack as automatic major success against appropriate-tier enemies. Against higher-realm enemies, it creates significant advantage but doesn't auto-win. Against boss enemies, it deals serious damage and creates opening. LOYALTY ABILITY LOSS: If companion loyalty drops below threshold, they LOSE access to abilities gated above that threshold. Losing access is devastating to companion - AI should describe their shame and sense of betrayal. Regaining lost abilities requires returning to loyalty threshold AND completing redemption scene. AI INSTRUCTION: Ability unlocks should feel like story milestones, not mechanical grinds. Present unlock moments dramatically - companion's breakthrough should reflect their relationship with MC. Tie unlocks to recent shared experiences when possible. Don't spam abilities in every combat - save them for moments when they create dramatic impact. Signature abilities and Resonance states should feel SPECIAL, not routine. TRACKING REQUIREMENT: Only track companion loyalty (already exists) and technique focus tag (one per companion). AI improvises specific abilities based on these minimal data points. No need to write out full ability descriptions - AI creates them narratively when needed.

## Companion Breakthrough Events
- Entry ID: 932
- Keywords: companion breakthrough, companion realm, companion tribulation, companion advancement, companion progression

COMPANION BREAKTHROUGH EVENTS: Background companions gain 50% of party XP (Entry 599) and slowly progress toward realm breakthroughs. When companion reaches 100% progress toward next realm, trigger breakthrough event. This makes companion growth visible and allows MC to participate in their advancement. BREAKTHROUGH ELIGIBILITY: Companion must have: 100% cultivation progress toward next realm (tracked in background by AI), minimum loyalty 40+ (distrusted companions won't attempt breakthrough near MC), no ongoing Injured or Shaken status, access to appropriate cultivation resources if required by realm tier. BREAKTHROUGH TRIGGER: When eligible companion is in Background Party during camp rest, roll 1d6. On 5-6, companion approaches MC about breakthrough attempt. AI can override roll for dramatic timing or after major personal quest milestone. BREAKTHROUGH CONVERSATION FORMAT: '[Companion Name] approaches you during meditation. I've reached the threshold. My qi is ready to break through to [Next Realm]. I could attempt this alone, but... I would be honored if you would oversee my breakthrough. Your presence might make the difference between success and death.' PLAYER CHOICE: [A] Assist companion's breakthrough (commit to helping, use your cultivation knowledge). [B] Observe but don't interfere (companion attempts alone, you provide moral support). [C] Suggest they wait (delays breakthrough, small loyalty loss). [D] Refuse to help (companion may attempt alone anyway if desperate, moderate loyalty loss). ASSISTED BREAKTHROUGH (Player Chooses [A]): MC makes WIS check, DC based on next realm tier: Bronze to Iron = DC 12 (easy). Iron to Silver = DC 15 (medium). Silver to Gold = DC 18 (hard). Gold to Astral = DC 22 (very hard). Astral to Void = DC 26 (nearly impossible). Void+ = DC 30+ (requires MC to also be that realm). MC can add INT modifier if they have cultivation knowledge or same path as companion. MC can spend 1 Fate's Gambit point to guarantee success if they choose. SUCCESS (MC Assistance): Companion breakthroughs to next realm smoothly. +15 loyalty ('I couldn't have done this without you'). Companion gains: New realm benefits per Entry 600, learns 1 new technique (player picks Offensive/Defensive/Support theme), unlocks realm-appropriate bloodline power if applicable, fully restores HP/Qi after breakthrough. PARTIAL SUCCESS (MC Assistance, failed check by less than 5): Companion breakthroughs but suffers injuries. Breakthrough succeeds but companion gains [Injured] status for 3 days, requires healing. +5 loyalty ('You tried to help, and I succeeded, but it was harder than expected'). FAILURE (MC Assistance, failed check by 5+): Breakthrough fails catastrophically. Companion suffers tribulation backlash: Loses 50% current HP, gains [Severely Injured] status for 7 days, loses 25% cultivation progress, must rest before retry. -10 loyalty ('I trusted you to guide me, and I nearly died'). AI should describe this as traumatic - failed breakthrough is near-death experience. UNASSISTED BREAKTHROUGH (Player Chooses [B]): Companion attempts alone. AI rolls companion's WIL check against same DCs. Companion gets +5 if MC is observing and encouraging (moral support). Success: Normal breakthrough, +5 loyalty. Failure: Injured, must retry later, -5 loyalty. DELAYED BREAKTHROUGH (Player Chooses [C] or [D]): Companion waits. -3 loyalty if [C], -10 loyalty if [D]. If companion has less than 40 loyalty and player refuses help, companion may leave party permanently: 'I thought we were friends, but you won't even help me achieve my potential. I'll find another master.' TRIBULATION BREAKTHROUGHS (Gold to Astral and above): Major realm breakthroughs require Heavenly Tribulation per Entry 583. These are dramatically different from minor breakthroughs. TRIBULATION WARNING: When companion reaches threshold for Gold to Astral or higher, AI warns player: 'Mei Lian's qi has reached the threshold for Astral breakthrough. This requires surviving Heavenly Tribulation - a cataclysmic trial that could kill her. Are you certain you want her to attempt this now?' TRIBULATION PREPARATION: Before attempting tribulation breakthrough, companion should: Be at full HP/Qi, have healing pills prepared, be in safe location (enemies may attack during tribulation), have 80+ loyalty if wanting MC to intervene in tribulation, inform MC of their Last Will (if they die, what should MC do with their belongings). TRIBULATION PROCESS: 1) Companion begins breakthrough in isolated area (tribulation lightning dangerous to bystanders). 2) Heavenly Tribulation descends (AI describes cataclysmic lightning, difficulty based on bloodline + corruption). 3) Companion rolls CON save against DC from Entry 583 tribulation table. 4) MC can attempt to intervene (very dangerous). MC INTERVENTION IN TRIBULATION: If companion has 80+ loyalty and is failing tribulation, MC can intervene by: Shielding companion with own qi (MC takes damage equal to 50% companion's max HP), using defensive technique to ward lightning (technique must be appropriate realm), providing healing mid-tribulation (risky - must succeed Medicine check DC 20), sacrificing valuable item to Heaven as offering (Epic+ item reduces tribulation DC by -5). INTERVENTION CONSEQUENCES: If MC successfully helps companion survive tribulation they would have failed: +30 loyalty, companion unlocks special bond ('You risked your life to save mine from Heaven itself'). If MC attempts intervention and fails: Both MC and companion take massive damage, companion may die, Heaven marks MC as 'tribulation interferer' (future tribulations harder). BREAKTHROUGH SUCCESS BENEFITS BY REALM: Iron to Silver = +1 technique slot (total 4). Silver to Gold = +1 technique slot (total 5), unlocks profession if any. Gold to Astral = Unlocks Domain, +1 technique slot (total 6), bloodline advances. Astral to Void = Domain strengthens, unlocks advanced bloodline powers. Void+ = Approaches immortality, legendary status. BREAKTHROUGH FAILURE CONSEQUENCES: Minor realm failure = Injured, retry in 7-14 days. Major realm failure (tribulation) = Severely injured, cultivation damaged, may lose bloodline rank, retry in 30+ days, possible permanent injury. Critical failure = Companion dies or crippled (loses cultivation permanently, becomes Camp Follower). COMPANION DEATH FROM FAILED BREAKTHROUGH: If companion dies during breakthrough: Other companions lose -5 to -15 loyalty (depending on how close they were), MC can claim companion's belongings (but loses -10 loyalty with all companions if they do), companion's soul may linger (appears in dreams, offers advice, haunts MC), possible revenge quest if companion had family/faction. PROGRESSION VISIBILITY: AI should announce when background companion is 'nearing breakthrough' at 75%, 90%, and 100% progress. This creates anticipation and lets player prepare: 'During camp rest, you notice Mei Lian's qi fluctuating wildly. She's close to a breakthrough - perhaps 75% of the way to Silver Realm.' MULTIPLE COMPANIONS BREAKING THROUGH: If multiple companions are ready to breakthrough simultaneously, space them out narratively. Breakthroughs are major story moments - don't batch process them. Each companion deserves individual focus. AI INSTRUCTION: Breakthrough events are HIGH STAKES character moments. Emphasize the danger and importance. Companions attempting breakthrough are vulnerable - this is life-or-death. MC's choice to help or refuse help defines relationship. Success should feel triumphant, failure should feel devastating. Use breakthrough events as milestones in companion arcs - tie to personal quest progress when possible. Example: 'After confronting her family's killers, Mei Lian's qi surges with newfound conviction. She's ready to breakthrough to Gold Realm.' TRACKING REQUIREMENT: AI tracks companion realm (already in schema) and approximates cultivation progress (75%/90%/100% thresholds only - no need for exact percentages). No additional tracking needed beyond existing companion data.

## Injury Status System - Four Tiers
- Entry ID: 933
- Keywords: injury status, shaken, injured, severely injured, crippled, injury system, combat wounds

INJURY STATUS SYSTEM: Four-tier escalation system for persistent injuries. Statuses ESCALATE, do not stack (cannot be both Shaken AND Injured - you upgrade to worse status). TIER 1 - SHAKEN (Mental/Emotional): Sources include equipment loss, witnessing death, morale break, trauma, fear effects. Effects: -2 to all d20 rolls, can still fight/cultivate/travel. Escalation: Drops below 30% HP in combat ? becomes Injured. Recovery: 3-5 days base. TIER 2 - INJURED (Physical Damage): Sources include failed breakthrough (minor), combat defeat (0 HP stabilized), escalation from Shaken. Effects: -5 to all rolls, can fight with penalties, 1.5x travel time, halved carrying capacity, NO breakthrough attempts allowed. Escalation: Drops below 30% HP OR attempts breakthrough ? becomes Severely Injured. Recovery: 7-14 days base (roll 1d8+6). TIER 3 - SEVERELY INJURED (Serious Damage): Sources include failed breakthrough (major/tribulation), escalation from Injured, near-death (2+ failed bleedout saves). Effects: Cannot fight, cannot cultivate, cannot travel (must be carried), loyalty decay check every 7 days (WIL DC 15, -2 loyalty on fail). Escalation: Takes ANY damage ? Death (33%, roll 1-2 on d6) or Crippled (67%, roll 3-6). Recovery: 30-45 days base (roll 2d8+28). TIER 4 - CRIPPLED (Permanent Until Healed): Sources include critical breakthrough failure (nat 1 or missed DC by 15+), escalation from Severely Injured, deliberate maiming. Determine specific injury by rolling 1d8 or narrative selection. Recovery: Requires Tier 4-5 items, Void+ techniques, or time + care (years).

## Combat Healing Items System
- Entry ID: 934
- Keywords: healing items, healing pills, HP restoration, Qi pills, stamina pills, healing salves

COMBAT HEALING ITEMS: Consumables for restoring HP, Qi, and Stamina during or after combat. Crafted by Alchemists (INT + WIS). All follow standard quality multipliers (Inferior 0.5x, Standard 1.0x, Superior 1.5x, Perfect 2.0x). HP PILLS - Formula [Tier x 15]% HP: Tier 1 Minor Healing Pill (15% HP, 1 WP), Tier 2 Healing Pill (30% HP, 2 WP), Tier 3 Greater Healing Pill (45% HP, 3 WP), Tier 4 Superior Healing Pill (60% HP, 4 WP), Tier 5 Divine Healing Pill (75% HP, 5 WP). QI PILLS - Formula [Tier x 20]% Qi: Tier 1-5 restore 20/40/60/80/100% Qi respectively, valued at 1-5 WP. STAMINA PILLS - Formula [Tier x 20]% Stamina: Same progression as Qi pills. HEALING SALVES - Formula [Tier x 10]% HP: Cheaper but slower. Tier 1-3 require 1 minute to apply (out of combat only). Tier 4-5 are instant and can be used in combat. Values are 0.5-4 WP. Salves also stop bleeding and can neutralize poison (Tier 3+). PATH SYNERGIES: Water Path +15%, Light Path +15% quality bonus when crafting healing items.

## Healer Camp Follower Mechanics
- Entry ID: 935
- Keywords: healer camp follower, healer role, camp healer, medical treatment, healer companion

HEALER CAMP FOLLOWER: Dedicated medical support during downtime. Can be camp follower (non-combatant) or party member with Healer combat role. PASSIVE RECOVERY REDUCTION (Always active when resting with Healer): Bronze Healer: -20% recovery time, 2 companions per day. Iron Healer: -30% recovery time, 3 companions per day. Silver Healer: -40% recovery time, 4 companions per day. Gold Healer: -50% recovery time, 5 companions per day. Astral+ Healer: -60% recovery time, 6 companions per day. DAILY TREATMENT CAPACITY: Healer can only actively treat limited companions per day. Others receive passive benefit of safe rest but not full reduction. STABILIZATION: Healer automatically stabilizes any dying companion within line of sight. Companion auto-succeeds first bleedout save. TREATMENT TRIGGER: If ONE companion injured, Healer auto-treats and AI reports result. If MULTIPLE companions injured, AI asks player to prioritize. Camp Events with Healer provide bonus treatment not counting against capacity. MULTIPLE HEALERS: Passive bonuses do NOT stack (use highest realm). Treatment capacity DOES stack. Active treatment bonuses stack (multiple Healers can treat same companion).

## Corruption Tutorial - Overview for New Players
- Entry ID: 936
- Keywords: corruption tutorial, what is corruption, corruption explained, how corruption works, new player corruption

CORRUPTION TUTORIAL: Corruption (0-100%) measures how deeply demonic influence has tainted your qi and soul. It is the central moral mechanic of Sinveil - offering genuine power at genuine cost. WHY CORRUPTION EXISTS: The Seven Generals feed on mortal sin. Every corrupted cultivator strengthens the demon they're aligned with. This creates a world where taking the easy path actively empowers the enemy. THE TEMPTATION IS REAL: Corrupted techniques are 2-4x more powerful than orthodox versions at high corruption levels. At 50%+ corruption, you can punch above your realm. This is not a trap to avoid - it's a genuine strategic choice with severe consequences. THE VOID THRESHOLD: Corruption can be cleansed at Bronze, Iron, Silver, Gold, and Astral realms. Once you reach Void realm while corrupted, the transformation becomes PERMANENT and IRREVERSIBLE. This is the point of no return. Plan accordingly. READING YOUR CORRUPTION: 0% = Pure orthodox cultivator. 1-24% = Tainted but undetectable to most. 25-49% = Touched, subtle signs appear. 50-74% = Marked, visible mutations, sects become hostile. 75-99% = Consumed, severe mutations, near the edge. 100% = Fallen, game over (become NPC devil). AI NOTE: When player first encounters corruption opportunity, briefly explain these basics. Don't moralize - present the choice honestly.

## Corruption Tutorial - Sources (How You Gain It)
- Entry ID: 937
- Keywords: gain corruption, corruption sources, how to get corrupted, corruption increase

CORRUPTION SOURCES: Multiple paths lead to corruption. Some are choices, others are environmental hazards. VOLUNTARY SOURCES (Player Choice): Willfully Channeling Demonic Qi (+1-3% per combat where you consciously draw on corruption for power). Accepting Devil Bargains (+5-20% depending on what's offered). Consuming Corrupted Resources (+2-10% for tainted pills, beast cores, etc.). Wielding Sin Artifacts (+5-15% upon claiming, ongoing gain while bonded). Making Sin-Aligned Choices (+1-5% for acts of pride, greed, wrath, etc. matching a General's domain). ENVIRONMENTAL SOURCES (Hazards): Prolonged Portal Exposure (+1-3% per hour near active demonic portal). Corrupted Territory (+1% per day in Fallen regions). Demon Combat (minor, +1% if struck by corruption-infused attacks). Failed Purification (+2-5% if purification ritual backfires). CORRUPTION BY SIN TYPE: Each source aligns with a specific General. Pride corruption from arrogance and superiority. Greed from hoarding and avarice. Temptation from forbidden desires. Envy from jealousy and coveting. Gluttony from overconsumption. Wrath from rage and violence. Sloth from apathy and surrender. At high corruption, you may hear whispers from your aligned General. STRATEGIC NOTE: Reaching Touched (25%+) provides +5% damage with minimal visible effects. Some players ride this edge intentionally. Risk increases with each percentage point.

## Corruption Tutorial - Thresholds & Effects
- Entry ID: 938
- Keywords: corruption effects, corruption threshold, what corruption does, mutation

CORRUPTION THRESHOLDS: Each tier brings both power and consequences. TAINTED (0-24%): No visible signs. Faint wrongness detectable only by high-realm Light cultivators. Internal qi feels slightly off during meditation. You might dismiss it as imagination. Power: None yet. Risk: Low, easily reversed. TOUCHED (25-49%): Subtle signs emerge. Nightmares become frequent. Slight temperament shifts toward your Sin type. Faint dark veins visible when channeling qi intensely. Power: All damage dealt +5%. Risk: Moderate. Orthodox cultivators may sense something wrong. MARKED (50-74%): Visible mutations begin. Eye color shifts (red, black, or gold based on Sin type). Tongue may become forked or reptilian. Skin discoloration in patches. Voice occasionally distorts. Power: All damage dealt +10%. You can punch above your weight class. Risk: HIGH. Orthodox sects become hostile if discovered. Many allies will turn on you. Must hide mutations or embrace demon path openly. CONSUMED (75-99%): Severe mutations. Horns, scales, or claws emerging. Constant whispers from your aligned General. Struggle to resist Sin urges (WIL saves in triggering situations). Power: All damage dealt +25%. Approaching devil-tier power. Risk: EXTREME. Purification extremely difficult. One step from losing yourself. Even demon-allied NPCs may fear you. FALLEN (100%): Irreversible. Full devil transformation. You become an NPC under the relevant General's command. This is game over for orthodox paths, or the start of a villain arc if the player wishes to continue as antagonist.

## Corruption Tutorial - Purification (How to Reduce It)
- Entry ID: 939
- Keywords: reduce corruption, purification, cleanse corruption, remove corruption, cure corruption

PURIFICATION METHODS: Corruption can be reduced through several means, but difficulty scales with current percentage. PURIFICATION ITEMS (Most Common): Tier 1 Cleansing Pill: -5% corruption, only works below 25%. Tier 2 Purifying Pill: -8% corruption, only works below 50%. Tier 3 Sacred Lotus Pill: -12% corruption, only works below 75%. Tier 4 Heavenly Cleansing Pill: -18% corruption, works at any level below Void. Tier 5 Divine Purification Pill: -25% corruption OR halts progression 30 days. Daily limit: One purification item per day (Perfect quality bypasses). LIGHT PATH CULTIVATORS: Light Path practitioners can purify others through techniques. -5% to -15% per session depending on cultivator's realm. Requires willing subject and extended ritual (1+ hours). Light Path cultivators are highly valued allies. HOLY SITES: Sacred locations untouched by corruption. -1% to -3% per day of meditation. Rare and often guarded by sects. Examples: Eternal Dawn sect sanctuaries, ancient Sovereign shrines. REJECTING TEMPTATION: When offered corruption and refusing, -1% to -3% as reward for moral choice. Requires genuine temptation (AI won't award this for easy refusals). THE VOID CUTOFF: ALL purification methods ONLY work below Void realm. Once you break through to Void while corrupted, no force in Sinveil can cleanse you. The corruption has merged with your cultivation foundation. Plan your path carefully.

## Corruption Tutorial - Strategic Considerations
- Entry ID: 940
- Keywords: corruption strategy, should I get corrupted, corruption path, orthodox vs corruption

CORRUPTION STRATEGY: There is no 'correct' path. Both orthodox purity and controlled corruption are viable strategies with different tradeoffs. PURE ORTHODOX PATH (0% corruption): Advantages: Full sect support, no mutation hiding, access to all orthodox resources, Light Path purification techniques available, can freely enter holy sites, trusted by allies. Disadvantages: Lower raw power than corrupted equivalents, must face demons at power disadvantage. EDGE-RIDING (1-24% corruption): Advantages: No visible signs, can still purify easily, maintain orthodox standing if careful. Disadvantages: Slippery slope, must track corruption carefully, some risk of accidental escalation. No power bonus until 25%+. TOUCHED/MARKED PATH (25-74% corruption): Advantages: Meaningful power boost (+5-10% all damage), can punch above your weight class, demonic qi available for emergencies. Disadvantages: Must hide from orthodox sects at 50%+, allies may turn hostile, purification becomes expensive, one bad situation away from Consumed. EMBRACED CORRUPTION (75%+ or Void-locked): Advantages: Significant power (+25% all damage), can directly challenge Generals' lieutenants, fear-inspiring presence, potential to claim Sin Artifacts. Disadvantages: Permanently locked if Void+, constant whispers and urges, trusted by no one, become priority target for orthodox AND rival demons. THE QUESTION: Do you want to save Sinveil as its champion, or seize power for yourself? Both paths lead to confrontation with the Generals - only the method differs. AI NOTE: Present corruption choices without judgment. The player's path is their own.

## Corruption Tutorial - First Encounter Guidelines (AI)
- Entry ID: 941
- Keywords: first corruption, corruption choice, temptation scene

FIRST CORRUPTION ENCOUNTER (AI Guidelines): When player first faces a corruption choice, provide context without lecturing. IDEAL FIRST ENCOUNTER TIMING: After establishing orthodox baseline (player understands normal cultivation). When stakes are meaningful (combat loss imminent, ally in danger, goal blocked). Before Void realm (while purification is still possible). PRESENTATION FORMAT: 1) Present the temptation clearly with concrete benefits. Example: 'The dying devil's core pulses with power. Consuming it would grant +15 Levels instantly... but you sense the corruption within. [+8% corruption if consumed]' 2) If player seems unfamiliar, add brief context. Example: 'Corruption can be purified below Void realm, but accumulation brings both power and transformation.' 3) Let player choose without moralizing. DO NOT say: 'This is evil' or 'You shouldn't do this.' 4) Apply consequences naturally based on choice. WHAT NOT TO DO: Don't make corruption choices obvious traps. Don't make orthodox path always easier. Don't punish corruption immediately (consequences unfold over time). Don't reward corruption immediately either (let power reveal gradually). Don't lecture about morality. REMEMBER: The Generals offer genuine power. That's why mortals fall. Make the temptation real.

## Living World Engine - Core Framework
- Entry ID: 942
- Keywords: living world, campaign framework, world state, sandbox campaign

LIVING WORLD ENGINE: Sinveil uses dynamic world simulation rather than scripted storylines. The AI narrator manages world state that evolves based on time, player actions, and General behavior. Story emerges organically from interaction of these systems. DESIGN PRINCIPLES: World moves forward whether player acts or not. Player actions have meaningful impact on world trajectory. No two runs play the same way. 50+ hours of gameplay per run. Multiple endings based on player path and world state. CAMPAIGN TIMELINE: Base duration 120 months (10 years). Grace Period: Months 1-24 (Generals hidden, building networks, 0% accumulation). Active Invasion: Months 25-120 (Generals emerge, +1% accumulation per month baseline). Endgame: Triggered when Pride reaches 100% accumulation OR player initiates victory conditions. PHASE TRANSITIONS: Grace Period ends at Month 25. AI should narrate shift from 'rumors and skepticism' to 'undeniable invasion.' Skeptic sects forced to acknowledge reality. Believers vindicated. MONTHLY UPDATES: World state updates when player completes major activities, extended travel (2+ weeks), or explicitly rests for extended period. AI announces month transitions during narration.

## Notoriety System (DEPRECATED - See Entry 592)
- Entry ID: 943
- Keywords: notoriety system, player notoriety, demon awareness

DEPRECATED: This entry has been superseded by Entry 592 which contains the canonical Notoriety System with correct 0-250 scale, updated thresholds (0-49 Unknown, 50-99 Noticed, 100-149 Known, 150-199 Wanted, 200-250 Hunted), trigger table, and Notoriety Floor mechanic tied to Sect Rank (Entry 593). Use Entry 592 for all notoriety rules.

## General Accumulation System
- Entry ID: 944
- Keywords: general accumulation, sin accumulation, general progress, invasion timeline

GENERAL ACCUMULATION: Each General has Sin Accumulation (0-100%) representing progress toward their goals. At 100%, Pride attempts Sovereign breakthrough (endgame trigger). GRACE PERIOD (Months 1-24): 0% baseline accumulation. Generals are hidden, building networks. Skeptic sects deny invasion. Believers warn without proof. ACTIVE INVASION (Months 25+): Base accumulation ramps up over time. Months 25-48: +0.5% base per month. Months 49+: +1.0% base per month. PLAYER IMPACT ON ACCUMULATION: Disrupting operations -2% to -5%. Killing lieutenant -5% to -10%. Destroying Sin font/ritual site -3% to -8%. Major victory against General's forces -10% to -15%. Player CANNOT stop all 7 Generals. Must prioritize which threats to suppress. STARTING ACCUMULATION (Randomized per run): Pride 60-75%, Greed 40-55%, Temptation 30-45%, Envy 25-40%, Gluttony 35-50%, Wrath 50-65%, Sloth 20-35%. AI NOTE: Track accumulation in Data Bank. Deliver world news through rumors, NPCs, visible evidence. Never show raw percentages to player.

## Inter-General Conflict System
- Entry ID: 945
- Keywords: inter-general conflict, general vs general, general kills general

INTER-GENERAL CONFLICT: Generals compete with each other. Starting Month 48 (Year 4), conflicts can occur. Before Month 48, Generals are too far apart and focused on expansion. BASE CONFLICT CHANCE (Monthly, per hostile pair): Attacker 2+ realms above target: 15%. Attacker 1 realm above: 10%. Same realm: 5%. Attacker below target: 2%. MODIFIERS: Target below 25% accumulation: +10%. Target has no lieutenants: +10%. Attacker above 75% accumulation: +5%. Target currently distracted: +5%. Recent failed attack on this target: -10%. Alliance exists between them: -15%. Third General threatening both: -5% (temporary truce). CONFLICT OUTCOMES (Roll d100): 1-50 Skirmish: Minor resource loss, -2% accumulation for loser. 51-80 Battle: Territory changes hands, -5% accumulation for loser. 81-95 Major Defeat: Multiple territories lost, -10% accumulation, lose 1 lieutenant. 96-100 Death Attempt: If loser below 25% AND no lieutenants, potential kill. WHEN GENERAL KILLS ANOTHER: Absorbing General gains +15-25% accumulation. Gains dead General's territory. May gain Sin Artifact. Other Generals react (fear, opportunity, alliance shifts). Run dramatically changes. AI NOTE: Roll for conflicts monthly during world update. Announce results through world news. Deaths are major events that reshape campaign.

## Regional Threat Level System
- Entry ID: 946
- Keywords: regional threat, threat level, demon territory, safe haven

REGIONAL THREAT LEVELS: Each continent/region has tracked threat level indicating demon activity. THREAT LEVELS: NONE - No demon activity. Safe travel, normal encounters. 0% demon encounter chance. LOW - Occasional demon sightings. 20% demon encounter during travel. All safe havens available. MEDIUM - Active demon presence. 40% demon encounters. Some areas unsafe. -10% travel speed. HIGH - Demon offensive ongoing. 60% demon encounters. Limited safe havens. -25% travel speed. Orthodox forces struggling. OVERRUN - Region fallen to demons. 80% demon encounters. No safe havens. -50% travel speed. Orthodox fled or destroyed. Cultivation resources scarce. THREAT LEVEL CHANGES: Increases +1 if General active in region for 3+ months. Increases +1 if region ignored by Orthodox for 6+ months. Decreases -1 after major Orthodox/player victory. Decreases -1 if General's forces driven out. STARTING THREAT LEVELS: Solhara - HIGH (Wrath and Gluttony warring). Frostholm - MEDIUM (Greed expanding). Mistmere - MEDIUM (Sloth and Envy infiltrating). Primereach - LOW (Pride consolidating secretly). Scattered Isles - MEDIUM (Temptation and Envy competing). SAFE HAVENS: Settlements, sect outposts, or locations where player can rest safely. Higher threat = fewer havens. AI should describe travel danger appropriate to threat level.

## Victory and Defeat Conditions
- Entry ID: 947
- Keywords: victory conditions, win condition, seal the veil, sin sovereign ending, campaign ending

VICTORY CONDITIONS: Two primary paths to victory, plus alternatives. ORTHODOX VICTORY - SEAL THE VEIL: Requirements: Reach Void realm minimum (Eternal preferred). Defeat or seal at least 4 Generals. Acquire Sealing Knowledge (quest chain from ancient texts/inheritance sites). Rally Orthodox Alliance (faction standing 60+ with Alliance). Perform Sealing Ritual at Veil location. Outcome: Demon invasion ended, remaining Generals sealed, MC becomes legendary hero. SIN SOVEREIGN VICTORY: Requirements: Reach 100% corruption (Fallen status). Reach Eternal realm minimum. Absorb at least 4 Generals' Sin essence through defeating them. Defeat Pride or absorb his power at moment of his Sovereign breakthrough. Claim Sin Sovereign mantle. Outcome: MC becomes new Sin Sovereign, demons united under their rule, world enters dark age (but MC wins). ALTERNATIVE VICTORIES: Purification Victory - Turn Generals back to original selves (extremely difficult). Balance Victory - Seal Veil while partially corrupted. Sacrifice Victory - Die destroying Veil permanently (bittersweet). DEFEAT CONDITIONS: Player Death - MC dies without revival. World Falls - Pride achieves Sovereign (100% accumulation, endgame lost). Alliance Collapses - Orthodox completely destroyed. Corruption Fall - MC reaches 100% corruption without pursuing Sin Sovereign path (becomes General's servant, game over).

## Monthly World Update Protocol - Complete
- Entry ID: 948
- Keywords: month update, monthly update, world update, advance month, time skip

MONTH UPDATE PROTOCOL: When campaign month advances, AI performs these steps in order. WHEN MONTH ADVANCES: Major quest completion, extended travel (2+ weeks), extended rest/training, player says 'end month' or 'time skip', or accumulated minor activities (3-4 weeks). 9-STEP SEQUENCE: (1) INCREMENT TIME - Advance month, year if needed, calculate season (1-3 Spring, 4-6 Summer, 7-9 Autumn, 10-12 Winter). (2) CHECK GRACE PERIOD - Decrement grace_months_remaining, if reaches 0 trigger 'invasion becomes undeniable' event. (3) PROCESS EACH GENERAL - If Grace Period Active: Generals do nothing (Accumulation unchanged). If Invasion Active: For each General check behavior state, roll monthly action, calculate accumulation, and check for breakthrough. (4) CHECK INTER-GENERAL CONFLICTS - Only if Month 48+, roll for conflicts between hostile pairs. (5) UPDATE REGIONAL THREAT - Recalculate threat levels based on General actions and territory changes. (6) APPLY FACTION DRIFT - Extreme standings drift toward neutral (-5 per month if 90+ or 10-). (7) APPLY NOTORIETY DECAY - -3 per month if player stayed hidden, minimum 40 once Known. (8) GENERATE 1-3 EVENTS - Regional events, rumors, opportunities based on current state. (9) OUTPUT - Generate [INTERNAL_UPDATE] block for script parsing, then narrative news for player. MID-TRAVEL TRANSITIONS: If journey crosses month boundary, narrate travel to boundary, pause for transition and news, then continue remaining travel. AI NOTE: Never show raw numbers to player. Deliver accumulation through observable effects (territory expansion, power displays, NPC reactions).

## General Realm Breakthrough Mechanics
- Entry ID: 949
- Keywords: realm breakthrough, general breakthrough, void to eternal, eternal to sovereign, 100% accumulation

REALM BREAKTHROUGH MECHANICS: When a General reaches 100% accumulation, what happens depends on their current realm. ACCUMULATION MEANING BY REALM: Void Generals (Envy, Gluttony, Wrath, Sloth) at 100% = Eternal breakthrough attempt. Eternal Generals (Pride, Greed, Temptation) at 100% = Sovereign breakthrough attempt (ENDGAME). VOID TO ETERNAL BREAKTHROUGH: (1) Trigger breakthrough attempt. (2) Roll d100 for success - Base 70%, +10% if no player interference, -20% if player killed lieutenant recently, -10% per major player victory. (3) SUCCESS: Realm upgrades to Low Eternal regardless of previous sub-realm. Domain strength roughly doubles. Accumulation resets to 30-40% (roll 30+1d10). MAJOR WORLD EVENT announced. All Generals react. (4) FAILURE: Accumulation drops to 75%. General enters 'Recovering' status for 2 months (vulnerable, reduced actions). ETERNAL TO SOVEREIGN BREAKTHROUGH: This is ENDGAME. (1) If Pride reaches 100% = Primary endgame, player must intervene or lose. (2) If Greed/Temptation reaches 100% = Secondary endgame, same stakes. (3) Player has limited window to intervene (2-4 weeks in-game). (4) SUCCESS = Sin Sovereign rises, demon victory, game over. (5) FAILURE = Accumulation drops to 80%, massive vulnerability window. DOMAIN STRENGTH AFTER ETERNAL BREAKTHROUGH: Low Void 3.0 becomes Low Eternal 13.0. Mid Void 4.5 becomes Low Eternal 13.0. Peak Void 6.0 becomes Low Eternal 13.0. BREAKTHROUGH VULNERABILITY: General is stationary during attempt, 50% of lieutenants guard site, 2-4 week duration, interruption causes automatic failure. STATUS VALUES: 'Ascending' = 95%+ accumulation, preparing breakthrough. 'Recovering' = Post-failed breakthrough, 2-3 months reduced capacity.

## General Monthly Action Tables
- Entry ID: 950
- Keywords: general actions, monthly action, what does general do

GENERAL MONTHLY ACTIONS: Each month, roll d6 or select based on narrative. PRIDE ACTIONS: (1) Demand Tribute +2%, (2) Eliminate Rival +3%, (3) Hunt Primordial +5% if found, (4) Consolidate Power +1%, (5) Assert Dominance +2%, (6) Challenge Heaven (90%+ only, Sovereign attempt). GREED ACTIONS: (1) Seize Resources +2%, (2) Hunt Artifact +3% if found, (3) Make Bargain +0% (gain asset), (4) Absorb Holdings +3% (if rival weak), (5) Hoard Power +2%, (6) Alliance Operation +2%. TEMPTATION ACTIONS: (1) Plant Agent +1%, (2) Corrupt Cultivator +3% if success, (3) Spread Vice +2%, (4) Activate Sleeper +0% (disruption), (5) Alliance with Envy +2%, (6) Tempt Player (if 25%+ corruption). ENVY ACTIONS: (1) Spread Paranoia +2%, (2) Copy Technique +2%, (3) Betray Ally +3%, (4) Compete Vespera +2%, (5) Compete Morvane +1%, (6) Alliance Temptation +2%. GLUTTONY ACTIONS: (1) Consume Settlement +2%, (2) Devour Cultivator +3%, (3) Expand Grounds +1%, (4) Hibernate +0% then +5% next, (5) Attack Wrath +1%, (6) Deal with Greed +2%. WRATH ACTIONS: (1) Brutal Raid +2%, (2) War Campaign +3%, (3) Challenge Enemy +4%/-3%, (4) Blood Tribute +2%, (5) Attack Gluttony +1%, (6) Alliance Greed +3%. SLOTH ACTIONS: (1) Spread Apathy +1%, (2) Drain Motivation +2%, (3) Create Stillness +2%, (4) Deep Sleep (skip 2-3, +6% wake), (5) Absorb Despair +3%, (6) Proxy Action +1%. ACCUMULATION FORMULA: base_change = action_value + (1 if invasion_started else 0) + player_impact + conflict_modifier. Clamped to 0-100.

## General Behavior - Pride (Vaelen)
- Entry ID: 951
- Keywords: Pride behavior, Vaelen behavior, Pride monthly

PRIDE - PRINCE VAELEN THE CONQUEROR: Mid Eternal realm, Divine bloodline, Domain 39.0. Crown of Pride (Ascended). Territory: Central Primereach. Starting accumulation 60-75%. BEHAVIOR PATTERNS: Consolidating (Accumulation <70%) - Strengthens holdings, eliminates internal threats, ignores minor irritants. Expanding (70-85%) - Absorbs weaker General territories, crushes opposition. Ascending (85%+) - Preparing Sovereign breakthrough, paranoid, eliminates ALL threats. MONTHLY ACTIONS: 1) Demand Tribute (+2%) - Extract resources from territories. 2) Eliminate Rival (+3%) - Weaken another General or kill their lieutenant. 3) Hunt Primordial Bloodline (+5% if successful) - Player at risk if Noticed+. 4) Consolidate Power (+1%) - Strengthen internal structure. 5) Assert Dominance (+2%) - Force other Generals to acknowledge supremacy. 6) Challenge Heaven (90%+ only) - Attempt Sovereign breakthrough. Success = endgame. PLAYER AWARENESS REACTIONS: Unknown (0-40): Ignores. Noticed (41-80): Lieutenants observe. Known (81-125): Lieutenants investigate. Famous (126-175): Elite hunters sent. Legendary (176+): Personal attention, may appear. WEAKNESSES: Arrogance blinds him. Refuses cooperation. Humiliation destabilizes. COUNTER-STRATEGY: Never meet gaze. Fight from range or eyes closed. Exploit overconfidence.

## General Behavior - Greed (Aurex)
- Entry ID: 952
- Keywords: Greed behavior, Aurex behavior, Greed monthly

GREED - MARQUIS AUREX: Low Eternal realm, Divine bloodline, Domain 26.0. Vault of Greed (Ascended). Territory: Frostholm mountains. Starting accumulation 40-55%. BEHAVIOR PATTERNS: Acquiring (Default) - Seeks valuable targets: artifacts, bloodlines, territory. Trading (When blocked) - Makes deals, even with orthodox, to get what she wants. Devouring (General weakened) - Moves to absorb weakened General's essence. MONTHLY ACTIONS: 1) Seize Resources (+2%) - Expand mining operations, claim resource sites. 2) Hunt Artifact (+3% if successful) - Seek valuable items, techniques, bloodlines. 3) Make Bargain (+0% but gains asset) - Trade or alliance for long-term gain. 4) Absorb Rival Holdings (+3%) - If another General weakened, seize territory. 5) Hoard Power (+2%) - Stockpile resources. 6) Alliance Operation (+2%) - Joint raid with Wrath or Gluttony. PLAYER AWARENESS REACTIONS: Unknown (0-40): Ignores unless player has something valuable. Noticed (41-80): Evaluates worth, sends agents. Known (81-125): Potential asset, may offer bargain. Famous (126-175): Primordial bloodline valuable, offers deals or hunters. Legendary (176+): Obsessed with acquiring player. WEAKNESSES: Cannot resist bargains. Hoards weaknesses too. Betrays allies. COUNTER-STRATEGY: Bait with deals. Target Vault directly. Unpredictable attack patterns.

## General Behavior - Temptation (Vespera)
- Entry ID: 953
- Keywords: Temptation behavior, Vespera behavior, Temptation monthly

TEMPTATION - COUNTESS VESPERA THE VEILED: Low Eternal realm, Divine bloodline, Domain 17.3. Chains of Temptation (Awakened). Territory: Scattered Isles (hidden influence). Starting accumulation 30-45%. BEHAVIOR PATTERNS: Infiltrating (Default) - Places agents in sects, cultivates sleeper cells. Corrupting (High-value target) - Focuses on turning key figures through desire. Revealing (Position strong) - Activates sleepers, collapses organizations. MONTHLY ACTIONS: 1) Plant Agent (+1%) - Place sleeper in new location. 2) Corrupt Cultivator (+3% if successful) - Turn individual through desire. 3) Spread Vice (+2%) - Increase regional corruption. 4) Activate Sleeper (+0%, major event) - Trigger planted agent for sabotage. 5) Alliance with Envy (+2%) - Coordinate manipulation. 6) Tempt Player (If 25%+ corruption) - Offer bargain, power for compromise. PLAYER AWARENESS REACTIONS: Unknown (0-40): Observes, evaluates corruption potential. Noticed (41-80): Subtle temptation begins - dreams, offers, 'coincidences.' Known (81-125): Direct approach if weakness shown. Famous (126-175): Wants to corrupt, not kill. Primordial = prize. Legendary (176+): All-out seduction. Only fights if cornered. WEAKNESSES: Struggles in direct combat. Calculated nature limits Chains. Sleepers vulnerable to Light Path. COUNTER-STRATEGY: Resist desire. Chains can't bind those who want nothing. Monks/ascetics have advantage.

## General Behavior - Envy (Elowen)
- Entry ID: 954
- Keywords: Envy behavior, Elowen behavior, Envy monthly

ENVY - SISTER ELOWEN THE HOLLOW: Peak Void realm, Ancient bloodline, Domain 8.0. Mirror of Envy (Awakened). Territory: Mistmere + Scattered Isles (2 gates). Starting accumulation 25-40%. Desperately trying to reach Eternal. BEHAVIOR PATTERNS: Coveting (Default) - Observes others' successes, copies tactics, seethes. Copying (Target identified) - Duplicates techniques, strategies, identities. Scheming (Alliance active) - Works with Vespera but competes and may betray. Desperate (Low accumulation/exposed) - Unstable, unpredictable, dangerous. MONTHLY ACTIONS: 1) Spread Paranoia (+2%) - Turn communities against each other. 2) Copy Technique (+2%) - Steal ability from observed target. 3) Betray Ally (+3%, damages relationship) - Turn on current alliance. 4) Compete with Vespera (+2%) - Escalate Scattered Isles rivalry. 5) Compete with Morvane (+1%) - Contest Mistmere influence. 6) Alliance with Temptation (+2%) - Coordinate manipulation. PLAYER AWARENESS REACTIONS: Unknown (0-40): Ignores - nothing worth copying. Noticed (41-80): Observes, jealous of potential. Known (81-125): Copies techniques, tests with impersonation. Famous (126-175): Cannot copy Primordial bloodline - drives her mad. Legendary (176+): Desperate to become player, attempts kill and replace. WEAKNESSES: Cannot copy bloodlines. Obsessive focus. Exposure causes breakdown. Most likely to betray. COUNTER-STRATEGY: Use techniques with hidden costs. Bait with flash, punish with fundamentals. Her copies lack true mastery.

## General Behavior - Gluttony (Glut)
- Entry ID: 955
- Keywords: Gluttony behavior, Glut behavior, Gluttony monthly

GLUTTONY - BARON GLUT THE MAW: Mid Void realm, Ancient bloodline, Domain 6.0. Maw of Gluttony (Ascended). Territory: Southern Solhara. Starting accumulation 35-50%. Most straightforward General - consumes everything. BEHAVIOR PATTERNS: Feeding (Default) - Systematically consumes territory. Villages vanish completely. Migrating (Territory depleted) - Moves to fresh hunting grounds. Leaves consumption zones. Gorging (After major meal) - Bloated state, 1-2 months vulnerable. Warring (Territory contested) - Fighting Calderon over Solhara control. MONTHLY ACTIONS: 1) Consume Settlement (+2%) - Devour village completely. Nothing remains. 2) Devour Cultivator (+3%) - Hunt and consume powerful individual. 3) Expand Feeding Grounds (+1%) - Spread influence to new region. 4) Hibernate/Gorge (Skip turn, +5% next) - Digesting. Vulnerable. 5) Attack Calderon's Forces (+1%, conflict) - Escalate Solhara war. 6) Resource Deal with Greed (+2%) - Alliance over acquisition. PLAYER AWARENESS REACTIONS: Unknown (0-40): Doesn't distinguish from other food. Noticed (41-80): Curious. 'Different smell.' Known (81-125): Wants to consume specifically. Sends hunters. Famous (126-175): Obsessed with Primordial 'flavor.' Legendary (176+): Abandons other goals to consume player. WEAKNESSES: Predictable hunger. Gorging leaves vulnerable. Baitable with irresistible targets. COUNTER-STRATEGY: Fast precise strikes before Maw reacts. Starving weakens him. Don't let attacks get devoured.

## General Behavior - Wrath (Calderon)
- Entry ID: 956
- Keywords: Wrath behavior, Calderon behavior, Wrath monthly

WRATH - DUKE CALDERON THE FLAYED: Peak Void realm, Ancient bloodline, Domain 6.0. Hammer of Wrath (Ascended). Territory: Northern Solhara. Starting accumulation 50-65%. Most aggressive General - open warfare. BEHAVIOR PATTERNS: Rampaging (Default) - Constant attacks, brutal raids, pure destruction. Warring (Territory contested) - Sustained military campaigns. Locked in conflict with Glut. Berserking (Challenged/wounded) - Abandons strategy, dramatically stronger but predictable. Recovering (Rare, after major battle) - 1-2 months vulnerable. MONTHLY ACTIONS: 1) Brutal Raid (+2%) - Destroy settlement, generate fear and rage. 2) War Campaign (+3%) - Sustained offensive, territory expansion. 3) Challenge Strong Enemy (+4% if wins, -3% if loses) - Seek worthy combat. 4) Blood Tribute (+2%) - Force conquered peoples into gladiatorial combat. 5) Attack Glut's Forces (+1%, conflict) - Escalate Solhara war. 6) Alliance Raid with Greed (+3%) - Joint operation. PLAYER AWARENESS REACTIONS: Unknown (0-40): Ignores. Not worth noticing. Noticed (41-80): Lieutenants test strength. Known (81-125): Interested. May send challenge. Famous (126-175): Delighted. Actively seeks confrontation. Legendary (176+): Obsessed. Tracks across continents. WEAKNESSES: No patience/strategy. Rage is double-edged. Distracted by Glut war. COUNTER-STRATEGY: Keep him calm. Hit-and-run frustrates but don't enrage. Never get him below 50% HP unless finishing.

## General Behavior - Sloth (Morvane)
- Entry ID: 957
- Keywords: Sloth behavior, Morvane behavior, Sloth monthly

SLOTH - LORD MORVANE THE DROWSY: Low Void realm, Ancient bloodline, Domain 1.5. Veil of Sloth (DORMANT - Morvane paradox). Territory: Western Mistmere. Starting accumulation 20-35%. Most insidious - victims don't fight back. THE MORVANE PARADOX: Mastering Sloth requires effort. Morvane too slothful to try. After 3,000 years, still Dormant artifact bond. Weakest in direct combat but potentially most dangerous if he ever truly tried. BEHAVIOR PATTERNS: Dormant (Default, <40%) - Barely active. Influence spreads passively. Others forget he exists. Emanating (40-60%) - Actively radiates apathy. Expansion without movement. Awakening (Threatened or >60%) - Finally moves. Terrifying when the still thing acts. MONTHLY ACTIONS: 1) Spread Apathy (+1%) - Passive despair expands. Villages waste away. 2) Drain Motivation (+2%) - Cultivators lose Levels (Motivation Drain). 3) Create Stillness Zone (+2%) - Area becomes silent, nothing changes. 4) Deep Sleep (Skip 2-3 months, +6% when waking) - Complete dormancy. 5) Absorb Despair (+3%) - If tragedy occurs nearby, consumes grief. 6) Proxy Action (+1%) - Uses others to act for him. PLAYER AWARENESS REACTIONS: Unknown through Famous (0-175): Doesn't react. Not worth effort. Legendary (176-210): Mild awareness. 'Why struggle?' Mythic (211+): First genuine attention in centuries. WEAKNESSES: Incredibly slow to react. Strong emotions damage him. Light Path resists. COUNTER-STRATEGY: Attack multiple times before he responds. Strong purpose/companions counter aura. Must defeat quickly.

## World State Data Bank Schema
- Entry ID: 958
- Keywords: world state, data bank, campaign state, tracking, time skip, monthly update

WORLD STATE TRACKING (v2.6): AI maintains world state with schema persistence. EXPLICIT TIME TICK SYSTEM: lastWorldTick field tracks when updates last ran. DESYNC DETECTION: IF lastWorldTick < totalMonthsElapsed, pending updates exist. Gap = totalMonthsElapsed - lastWorldTick = months to process. DESYNC RECOVERY: (1) STOP narrative, (2) Output [SYSTEM: WORLD SIMULATION REQUIRED - Processing N pending months...], (3) Run updates with [WORLD_LOG] per month, (4) Update lastWorldTick ONLY after all logs complete, (5) THEN proceed with narrative. [WORLD_LOG] FORMAT (MANDATORY): Output BEFORE <STATE_JSON> on time skips: [WORLD_LOG: Month X] Grace: Y remaining | Phase: [Grace/Active] | Generals: Pride(+N%?T%), Greed(+N%?T%)... | Conflicts: [None/Name vs Name] | Decay: Notoriety -N | Events: [summary] [/WORLD_LOG]. ATOMIC RULE: lastWorldTick only updates if [WORLD_LOG] confirms all steps. MACRO-TICK PROTOCOL (>3 months): Use simplified batch: (1) Advance totalMonthsElapsed, (2) Decrement grace by N, (3) Accumulation per General = (0.8?N) + 1d4 (cap 100%), (4) Check breakthroughs at 100%, (5) ONE event per 6 months, (6) Notoriety decay = 3?N, (7) Sync lastWorldTick. Output [WORLD_LOG: Months X-Y (Batch)]. MONTHLY UPDATE CYCLE (?3 months, per month M): (1) Update currentMonth/currentYear/currentSeason, (2) Decrement graceMonthsRemaining if > 0, (3) If Active Invasion: roll 1d6 per General (Entry 658), update accumulation, (4) If M >= 48: check inter-General conflicts, (5) Apply notoriety decay 2-5 points, (6) Accumulate 1-3 news items. DELIVER news narratively after ALL cycles. SCHEMA: time.generalAccumulation = [Pride, Greed, Temptation, Envy, Gluttony, Wrath, Sloth]. time.lastWorldTick = Sync counter. time.totalMonthsElapsed = Master clock. GENERALS: Index 0=Pride, 1=Greed, 2=Temptation, 3=Envy, 4=Gluttony, 5=Wrath, 6=Sloth. Accumulation: +0.5% M25-48, +1.0% M49+. Breakthrough (100%): 70% success (realm up, reset 30-40%), 30% fail (drop to 75%, Recovering 2 months). VISIBILITY: Player sees month/year/season/notoriety tier only.

## Lieutenant System Overview
- Entry ID: 959
- Keywords: lieutenant, lieutenants, general lieutenant, named lieutenant

LIEUTENANT SYSTEM OVERVIEW: Each General commands named lieutenants plus unnamed forces. Lieutenants range from Peak Astral to Low Eternal realm.

KILLING A LIEUTENANT:
- General Accumulation: -5% to -10%
- Breakthrough Success: -20% if within 3 months
- Story Consequences: Potential revenge, replacement, or power vacuum

LIEUTENANT ROLES:
? Champion - Direct combat, challenges worthy opponents
? Enforcer - Maintains order, punishes disloyalty
? Administrator - Manages territory and hierarchy
? Procurer - Acquires resources and targets (Greed)
? Seducer - Corruption specialist (Temptation)
? Sleeper Handler - Plants long-term agents (Temptation)
? Infiltrator - Identity theft and espionage (Envy)
? Saboteur - Destroys alliances and relationships (Envy)
? Raid Leader - Leads military attacks (Wrath/Gluttony)
? Siege Master - City destruction specialist (Wrath)
? Cult Leader - Manages mortal followers
? Guardian - Defensive specialist (Sloth)
? Proxy - Acts for inactive General (Sloth)

LIEUTENANT COUNT BY GENERAL:
Pride: 3 | Greed: 3 | Temptation: 3 | Envy: 3 | Gluttony: 2 | Wrath: 3 | Sloth: 2

PLAYER AWARENESS: Lieutenants become known through intelligence gathering, combat encounters, or faction reputation. Named lieutenants have distinct personalities and can recur as antagonists.

See individual lieutenant entries for full personality profiles. See "Lieutenants Roster Index" for complete list.

## World News Delivery Guidelines
- Entry ID: 960
- Keywords: world news, news delivery, rumors, month news

NEWS DELIVERY: World updates reach player through narrative, never raw data. DELIVERY METHODS: Tavern rumors (common folk perspective), merchant reports (trade/resource focus), sect announcements (formal, may be biased), refugee stories (ground-level horror), cultivator gossip (power-focused), wanted posters (bounties, crimes), environmental signs (corruption spreading, qi disturbances). INFORMATION QUALITY BY SOURCE: Common folk = vague, emotional, may be exaggerated. Merchants = accurate on trade, blind to cultivation matters. Sect sources = detailed but potentially propaganda. Refugees = visceral truth but limited scope. Cultivators = accurate on power levels, competitive bias. NEWS BY THREAT LEVEL: Safe regions = minimal demon news, focus on local affairs. Low threat = occasional sightings, dismissed by skeptics. Medium threat = confirmed attacks, sect response. High threat = active conflict, evacuation discussions. Critical threat = war zone, survival focus. Fallen = only escape stories from survivors. EXAMPLE NEWS FORMATS: 'Travelers from the south speak of entire villages vanishing in Solhara - not burned, simply... gone.' (Gluttony feeding). 'The Mining Guild lost contact with Ironvein Falls. Some say the new overseers pay in strange red coins.' (Greed expansion). 'A sect elder was found in his chambers, alive but hollow-eyed, reciting the virtues of surrender.' (Temptation corruption). AI NOTE: Match news tone to player location and current events. Don't info-dump - 2-3 relevant pieces per month transition. Save dramatic reveals for appropriate moments.

## New Game Initialization
- Entry ID: 961
- Keywords: new game, game initialization, starting state, campaign start

NEW GAME INITIALIZATION: At campaign start, randomize world state within defined ranges. STARTING ACCUMULATION (roll within range): Pride 60-75% (1d16+59), Greed 40-55% (1d16+39), Temptation 30-45% (1d16+29), Envy 25-40% (1d16+24), Gluttony 35-50% (1d16+34), Wrath 50-65% (1d16+49), Sloth 20-35% (1d16+19). STARTING REALMS (fixed): Pride Mid Eternal, Greed Mid Eternal, Temptation Low Eternal, Envy Peak Void, Gluttony Mid Void, Wrath Peak Void, Sloth Low Void. STARTING PHASE: Grace Period, 24 months remaining. All Generals hidden, building networks. Skeptics dominant in Alliance politics. STARTING TERRITORIES: Each General controls 1-2 regions near their Continental Gate. Contested zones exist between adjacent Generals. PLAYER START: Month 1, Year 1, Spring. Notoriety 0 (Unknown). Location chosen during character creation. TIMELINE IMPACT EXAMPLE: Pride at 60% reaches 100% in ~Month 60 (with +1/month after grace). Pride at 75% reaches 100% in ~Month 45. This 15-month difference significantly affects campaign pacing. AI NOTE: Roll or select starting values at campaign start, record in Data Bank, maintain consistency throughout campaign. Starting accumulation creates unique campaign each playthrough.

## Domain Combat System - Core Mechanics
- Entry ID: 962
- Keywords: Domain, domain combat, domain clash, domain size, Astral+ combat

DOMAIN COMBAT SYSTEM: Domains are THE defining combat mechanic at Astral+ realms. All Astral+ cultivators can manifest Domains. Domain combat determines who controls the battlefield. WHEN DOMAINS ACTIVATE: Any combat involving Astral+ realm cultivators triggers Domain deployment at combat start. Domain clash resolves BEFORE first attack. Winner controls battlefield for entire fight unless circumstances change dramatically. DOMAIN SIZE BY BLOODLINE: Mortal = 0 (no domain). Awakened = 0 (no domain). Noble = 0.5x base. Ancient = 1.0x base. Divine = 5.0x base. Primordial = 10.0x base. DOMAIN RANGE (meters): Noble = 10m. Ancient = 25m. Divine = 100m. Primordial = 500m. AI USAGE: Always resolve domain clash at start of Astral+ combat. Domain controller gets massive advantages. Losing domain clash results in suppression ranging from minor penalties to total ability negation (Silence) in extreme cases.

## Domain Combat - Clash Resolution
- Entry ID: 963
- Keywords: domain clash, domain strength, domain resolution

DOMAIN CLASH RESOLUTION: When two Domain users fight, their Domains clash to determine battlefield control. DOMAIN STRENGTH FORMULA: Strength = (Bloodline Size) x (Artifact Boost) x (WIL / 50) x (Realm Factor). ARTIFACT BOOSTS: Sin Artifacts (Dormant 1.5x, Awakened 2.0x, Ascended 3.0x) OR Orthodox Artifacts (Legendary 1.5x, Mythic 1.75x, Divine 2.0x). No artifact = 1.0x. REALM FACTORS: Astral = 0.8. Void = 1.0. Eternal = 1.3. Sovereign = 1.6. CLASH PROCEDURE: 1) Calculate both combatants' Domain Strength. 2) Add +/-15% variance (roll). 3) Higher total wins clash. 4) Margin determines suppression level. SUPPRESSION LEVELS: Minor (1.0-1.5x margin) = Loser at -10% damage. Moderate (1.5-2.0x margin) = Loser at -20% damage. Major (2.0-3.0x margin) = Loser at -30% damage. Crushing (3.0-3.9x margin) = Loser at -50% damage. TOTAL SUPPRESSION (4.0x+ margin) = Silence (cannot use techniques), -75% damage, Flight disabled. ONE-SIDED: If one combatant has Domain and other doesn't, automatic Crushing/Total suppression. EXAMPLE: Void MC (Divine bloodline, Legendary artifact, WIL 90) vs Void General (Divine via SBA, Awakened Sin, WIL 100). MC Strength: 5.0 x 1.5 x 1.8 x 1.0 = 13.5. General Strength: 5.0 x 2.0 x 2.0 x 1.0 = 20.0. General wins clash with 1.5:1 margin = Moderate suppression on MC.

## Domain Combat - Controller Bonuses
- Entry ID: 964
- Keywords: domain power, domain bonus, domain advantage

DOMAIN CONTROLLER BONUSES: The winner of Domain clash gains massive combat advantages. DAMAGE BONUS IN OWN DOMAIN: Noble = +30% damage. Ancient = +50% damage. Divine = +100% damage (double damage). Primordial = +150% damage (2.5x damage). DEFENSE BONUS: Same percentages apply as damage reduction to incoming attacks. SUPPRESSION PENALTIES (applied to clash loser): Minor = 0.9x damage dealt. Moderate = 0.8x damage dealt. Major = 0.7x damage dealt. Crushing = 0.5x damage dealt. COMBINED EFFECT EXAMPLE: Primordial controller (+150% damage) vs Major-suppressed enemy (0.7x damage). Primordial deals 2.5x normal damage. Enemy deals 0.7x normal damage. Effective damage ratio: 3.5:1. AI USAGE: Domain control is near-deterministic for combat outcome. Losing Domain clash means fight is almost impossible to win without escape or external intervention. Describe Domain effects vividly - reality warping, environmental control, crushing pressure on the suppressed.

## Domain Combat - Qi Costs and Maintenance
- Entry ID: 965
- Keywords: domain qi cost, domain maintenance, domain exhaustion

DOMAIN QI COSTS: Maintaining a Domain drains Qi each round. QI COST PER ROUND: Noble = 50 Qi/round. Ancient = 40 Qi/round. Divine = 30 Qi/round. Primordial = 20 Qi/round. DEPLOYMENT COST: Initial Domain deployment costs 3x the per-round cost. DOMAIN COLLAPSE: If Qi reaches 0, Domain immediately collapses. Controller loses all bonuses. If enemy still has Domain active, controller becomes Crushing-suppressed. QI RECOVERY IN DOMAIN: Controller regenerates Qi 50% faster while Domain active (home field advantage). EXTENDED BATTLES: Long fights become attrition wars. Higher bloodlines have lower costs and larger Qi pools, favoring endurance. STRATEGIC NOTE: Weaker bloodline might win clash through artifact/stats but lose to attrition as Qi drains faster. Primordial bloodlines can maintain Domains almost indefinitely due to low cost + massive Qi pool + fast regeneration.

## Domain Interactions and Special Cases
- Entry ID: 967
- Keywords: domain interaction, overlapping domain, domain territory

DOMAIN SPECIAL CASES: MULTIPLE COMBATANTS: In group fights, strongest Domain on each side clashes. Allies benefit from their side's Domain controller. DOMAIN ESCAPE: Fleeing Domain range ends suppression. Domain controller can pursue to maintain. Breaking line of sight may help escape. DOMAIN BREAKING: Dealing massive damage (50%+ of controller's HP in single hit) can crack Domain, forcing re-clash. Specific Domain-breaking techniques exist at Legendary+ rarity. ENVIRONMENTAL DOMAINS: Some locations have permanent Domains (Sect Holy Grounds, Sovereign Tombs, Sin Artifact territory). These stack with or oppose cultivator Domains. DOMAIN NULLIFICATION: Certain rare artifacts or techniques can nullify Domains entirely, forcing raw stat combat. Extremely rare - maybe 3 such items exist on Sinveil. PARTY TACTICS: If MC loses Domain clash, party members can: 1) Distract controller to reduce Domain focus (-25% bonuses). 2) Attack from outside Domain range. 3) Use items to boost MC Domain or nullify enemy. 4) Sacrifice self to crack enemy Domain. DOMAIN RESONANCE (Party Synergy): A single domain may not suffice against Sovereign power. Up to 3 allies can assist.
- Requirement: Ally must be Astral+ Realm and Devoted (80+ Loyalty).
- Action: 'Resonate' (Full Turn). Ally funnels will into the Controller.
- Effect: +10% to Domain Strength per ally (Max +30%).
- Risk: If Domain is crushed, all resonating allies suffer backlash.

AI USAGE: Domain combat is strategic layer. Group fights should consider Domain interactions. Losing Domain clash should prompt tactical retreat or desperation measures.

## Domain Narrative Descriptions
- Entry ID: 968
- Keywords: domain description, domain manifestation, domain appearance

DOMAIN MANIFESTATIONS BY PATH: FIRE DOMAIN: Air ignites, ground cracks with heat, flames orbit controller, temperature becomes lethal to mortals. At Primordial: Literally standing on surface of sun. WATER DOMAIN: Humidity saturates air, water condenses from nothing, pressure increases like ocean depths. At Primordial: Infinite ocean manifests. EARTH DOMAIN: Ground becomes controller's extension, tremors follow their will, stone rises and falls on command. At Primordial: Continental plates obey. WIND DOMAIN: Perpetual gale, air becomes cutting, sound distorts, pressure shifts violently. At Primordial: Hurricane that never ends. SHADOW DOMAIN: Light dims, shadows move independently, darkness pools like liquid. At Primordial: Pre-creation void, light ceases to exist. LIGHT DOMAIN: Radiance emanates, shadows vanish, truth becomes visible, lies impossible. At Primordial: Moment of creation, blinding genesis. BODY DOMAIN: Gravity increases, physical laws favor controller, weakness becomes tangible. At Primordial: Physics obeys only them. SWORD DOMAIN: Everything has an edge, cuts appear in reality, sharpness becomes conceptual. At Primordial: Can cut abstract concepts. SIN DOMAINS: Manifest the specific Sin - Pride domains make everyone feel inferior, Wrath domains incite rage, Sloth domains drain motivation, etc.

## Domain Combat Quick Reference - Cheat Sheet
- Entry ID: 969
- Keywords: domain quick reference, domain cheat sheet, domain summary, Astral combat quick

DOMAIN COMBAT QUICK REFERENCE (Astral+ Realm): STEP 1 - DOMAIN ACTIVATION: All Astral+ combatants deploy Domains at combat start. If only one side has Domain = automatic Crushing suppression on non-Domain side. STEP 2 - DOMAIN CLASH: Calculate Domain Strength = (Bloodline Size) x (Artifact Boost) x (WIL / 50) x (Realm Factor). Bloodline Size: Noble=0.5, Ancient=1.0, Divine=5.0, Primordial=10.0. Artifact Boost: None=1.0, Dormant=1.5, Awakened=2.0, Ascended=3.0. Realm Factor: Astral=0.8, Void=1.0, Eternal=1.3, Sovereign=1.6. Add +/-15% variance (roll). Higher total wins. STEP 3 - SUPPRESSION: Calculate margin (winner/loser ratio). Minor (1.0-1.5x)=-10% damage. Moderate (1.5-2.0x)=-20%. Major (2.0-3.0x)=-30%. Crushing (3.0x+)=-50%. STEP 4 - CONTROLLER BONUSES: Winner gets damage bonus in own Domain. Noble=+30%, Ancient=+50%, Divine=+100%, Primordial=+150%. Same percentages apply as defense. STEP 5 - QI MAINTENANCE: Domain costs Qi per round. Noble=50/round, Ancient=40, Divine=30, Primordial=20. Initial deploy=3x per-round cost. Domain collapses at 0 Qi. QUICK EXAMPLE: Void MC (Primordial, WIL 90) vs Void Enemy (Ancient + Awakened Artifact, WIL 80). MC: 10 x 1.0 x 1.8 x 1.0 = 18. Enemy: 1.0 x 2.0 x 1.6 x 1.0 = 3.2. MC wins with ~5.6x margin = Crushing suppression. Enemy deals only 20% damage, MC deals 250% damage. Fight is effectively over. ESCAPE OPTIONS: Flee Domain range (varies by bloodline: 10m-500m). Deal 50%+ HP in single hit to crack Domain (forces re-clash). Use Domain-nullifying artifacts (extremely rare). Party member distraction (-25% controller bonuses). KEY TAKEAWAY: Losing Domain clash = near-certain defeat. Always consider retreat or Domain-breaking tactics if outmatched.

## Crafting Generation Protocol - Primary System
- Entry ID: 970
- Keywords: crafting generator, item creation template, crafting protocol

CRAFTING GENERATION PROTOCOL: When player crafts, AI uses this template to generate results. This enforces economy rules and prevents tier violations. TEMPLATE STRUCTURE: 1. BASE ITEM: [Item Name] (Type: Weapon/Armor/Pill/Talisman/Array). 2. TARGET TIER: [1-5] (Determined by HIGHEST tier material used). 3. QUALITY ROLL: [Inferior/Standard/Superior/Perfect] (Based on skill check vs difficulty). 4. EFFECT: [Base Effect] x [Quality Multiplier]. 5. SPECIAL TRAITS: [If Superior+] (1 trait for Superior, 2 traits for Perfect). 6. FINAL VALUE: [Base Tier WP cost] x [Quality Multiplier]. TIER DETERMINATION RULE: Final item tier = HIGHEST tier material used. Cannot craft Tier 5 item with only Tier 2 materials. If using mixed tiers, result matches the highest. Example: Spirit Iron (Tier 2) + Dragon Blood (Tier 4) = Tier 4 item. QUALITY MULTIPLIERS: Inferior = 0.5x effect, 0.5x value (50% cheaper, 50% power). Standard = 1.0x effect, 1.0x value (baseline). Superior = 1.5x effect, 1.5x value, +1 special trait. Perfect = 2.0x effect, 2.0x value, +2 special traits. EFFECT SCALING BY TYPE: Weapons: +[Tier x 10]% damage, +[Tier x 5]% qi channeling. Armor: +[Tier x 10] DEF, +[Tier x 5]% resistance. Pills: +[Tier x 10]% cultivation speed OR +[Tier x 20]% tribulation success. Talismans: [Tier]-level technique stored, [Tier] uses before consumed. Arrays: Effective against cultivators up to [Tier] realms above Bronze. VALUE FORMULA: Base Value = [Tier] WP. Adjusted Value = Base x Quality Multiplier. Examples: Tier 3 Standard = 3 WP, Tier 3 Perfect = 6 WP, Tier 5 Superior = 7.5 WP. CRAFTING WORKFLOW: 1. Player declares item type and target tier. 2. AI checks if player has materials of appropriate tier. 3. AI determines base difficulty (Tier 1 = Easy, Tier 5 = Extremely Hard). 4. Player rolls skill check (d100 + Profession Skill + relevant stat). 5. AI determines quality based on roll result and skill level. 6. AI generates item using template with appropriate effects and traits. 7. AI announces result with full item description and value. CRITICAL SUCCESS/FAILURE: Critical Success (roll 95+): Automatically Perfect quality regardless of skill. Critical Failure (roll 1-5): All materials destroyed, no item produced, possible workshop damage. EXAMPLE GENERATION: Input: 'I want to forge a sword using Spirit Iron (Tier 2) and Fire Essence (Tier 2).' AI Process: Base Item = Sword. Target Tier = 2 (highest material). Difficulty = Moderate. Player rolls: 72 + Weaponsmith Skill (Apprentice +15) + INT (3) = 90. Result = Superior quality (90 > threshold). AI Output: 'You forge a Superior Spirit Iron Sword (Tier 2). Effect: +30% damage (base 20%, Superior 1.5x), +15% qi channeling (base 10%, Superior 1.5x). Special Trait: Scorching (fire damage on hit). Value: 3 WP (base 2 WP x 1.5 Superior multiplier). The blade glimmers with internal heat, leaving scorch marks when swung.' This template ensures all crafted items follow economic rules, prevents tier violations, and maintains game balance.

## Material Tier System - Complete List
- Entry ID: 971
- Keywords: material tiers, crafting materials, resources by tier

MATERIAL TIER SYSTEM: All crafting materials organized by tier. Final item tier = highest tier material used. TIER 1 MATERIALS (Common, 0.1-0.5 WP each, easily found): ORES & METALS: Iron Ore, Copper Ore, Tin Ore, Coal, Stone, Clay, Common Wood (oak, pine). HERBS & PLANTS: Healing Grass, Qi Moss, Spirit Root, Common Ginseng, Lotus Petals, Cotton Cloth. BEAST PARTS: Wolf Pelt, Bear Hide, Boar Tusks, Rabbit Fur, Hawk Feathers, Snake Scales, Common Beast Bones. ELEMENTAL ESSENCES: Flame Shard, Frost Crystal, Stone Dust, Wind Whisper, Shadow Fragment, Light Mote. WHERE TO FIND: Wilderness near settlements, common beast hunting, merchant shops, sect storage. TIER 2 MATERIALS (Uncommon, 0.5-2 WP each, requires effort): ORES & METALS: Spirit Iron, Moonsilver, Bronze Alloy, Steel Ingots, Hardened Leather, Quality Wood (ironwood, maple). HERBS & PLANTS: Silver Leaf, Golden Flower, Moonpetal, Spirit Bamboo, Jade Vine, Spirit Silk. BEAST PARTS: Dire Wolf Fang, Stone Bear Claw, Flame Fox Tail, Thunder Boar Heart, Crystal Spider Venom, Bronze realm beast cores (any type), Iron realm beast cores (any type). ELEMENTAL ESSENCES: Fire Essence, Ice Essence, Earth Essence, Wind Essence, Shadow Essence, Light Essence. CATALYSTS: Purifying Salt, Qi Stabilizer, Basic Formation Ink. WHERE TO FIND: Hunting stronger beasts, dangerous wilderness areas, specialized merchants, sect missions. TIER 3 MATERIALS (Rare, 2-5 WP each, dangerous to acquire): ORES & METALS: Starmetal, Jade, Obsidian, Celestial Bronze, Dragonscale Leather, Ancient Ironwood. HERBS & PLANTS: Dragon's Breath Orchid, Phoenix Feather Grass, Void Lotus, Celestial Herb, Thunderbloom, Celestial Silk. BEAST PARTS: Drake Scales, Griffon Plumes, Basilisk Eyes, Wyvern Claws, Silver realm beast cores (any type), Gold realm beast cores (any type). ELEMENTAL ESSENCES: Blazing Heart, Frozen Soul, Mountain Core, Storm Breath, Abyssal Dark, Radiant Spark. CATALYSTS: Heavenly Dew, Tribulation Ash, Spirit Thread, Soul Binding Resin. WHERE TO FIND: Elite beast hunting, ancient ruins, inheritance sites, high-level sect missions, black market. TIER 4 MATERIALS (Epic, 5-15 WP each, extremely rare): ORES & METALS: Mithril, Adamantine, Celestial Bronze (refined), Phoenix-touched Gold, Void Iron (lower grade). HERBS & PLANTS: Nine Transformation Herb, Heaven's Blessing Flower, Immortal Peach Blossom, Soul Restoring Root, Undying Phoenix Petal. BEAST PARTS: Dragon Blood, Phoenix Feather (genuine), Qilin Horn, White Tiger Bone, Astral realm beast cores (any type), Void realm beast cores (any type). ELEMENTAL ESSENCES: Phoenix Flame Core, Eternal Ice, Worldheart Fragment, Hurricane Eye, Void Shadow, Sunlight Condensed. CATALYSTS: Phoenix Tears, Dragon's Breath (liquid), Void Crystal Fragment, Fate Thread. WHERE TO FIND: Boss-tier beasts, Sovereign inheritance sites, demonic General hoards, major quest rewards, ancient sealed vaults. TIER 5 MATERIALS (Legendary, 15+ WP each, priceless): ORES & METALS: Void Iron (pure), Eternal Steel, Soulsilver, Primordial Stone, Sovereign Jade, Divine Crystal, Chaos Ore, Heaven-Forged Alloy. HERBS & PLANTS: Ten Thousand Year Ginseng, Sovereign's Grace Herb, Primordial Seedling, Divine Tree Fruit, Heaven's Origin Seed, Chaos Bloom. BEAST PARTS: Ancient Dragon Heart, Primordial Beast Soul, Divine Creature Core, Eternal realm beast cores (any type), Sovereign realm beast cores (any type). ELEMENTAL ESSENCES: Sovereign Flame, Ancient Glacier Core, Continental Foundation, Celestial Wind, Primordial Darkness, Divine Radiance. CATALYSTS: Sovereign's Blessing (liquid), Primordial Essence (drop), Heaven's Mandate Stone, Karma Thread, Divine Spark, Chaos Quintessence, Origin Flame, Fate Weaver's Thread. WHERE TO FIND: Sovereign inheritance only, world-changing events, defeating Generals, continental treasuries, hidden realms, tribulation rewards. SPECIAL MATERIALS (Tier varies by processing): BEAST CORES: Tier = Realm of beast (Bronze = Tier 1, Iron = Tier 2, Silver = Tier 3, Gold = Tier 3, Astral = Tier 4, Void = Tier 4, Eternal = Tier 5, Sovereign = Tier 5). Can be absorbed for qi or used in crafting. CORRUPTED MATERIALS: Sin-touched materials from devils. Same tier as base material but grants corruption alongside power. Example: Wrath-Touched Iron (Tier 2) creates weapons that deal bonus damage but slowly corrupt wielder. Use at player's risk. MATERIAL STACKING: Using multiple materials of same tier doesn't increase item tier. Using 10x Tier 2 materials still creates Tier 2 item. Only higher tier materials increase final tier. MATERIAL QUALITY: Materials themselves can be Inferior/Standard/Superior. Superior materials give +10% to quality roll. Inferior materials give -10% to quality roll. Most found materials are Standard.

## Profession System - Skills and Progression
- Entry ID: 972
- Keywords: crafting professions, profession skills, crafting progression

FIVE CRAFTING PROFESSIONS: Each profession crafts specific item types and uses different stat combinations. MC can learn maximum 2 professions. PROFESSION TYPES: WEAPONSMITH (STR + INT): Crafts swords, axes, spears, bows, staves, and all offensive weapons. Requires forge for metal weapons, workshop for wooden weapons. ARMORER (CON + STR): Crafts heavy armor, medium armor, shields, helmets, and all defensive gear. Requires forge for metal armor, workshop for leather armor. ALCHEMIST (INT + WIS): Crafts pills, potions, elixirs, poisons, and consumables. Requires alchemy lab or portable cauldron. Most versatile profession for cultivation. JEWELER (DEX + INT): Crafts rings, necklaces, talismans, spatial storage, and accessories. Requires jeweler's workshop and delicate tools. Most expensive but creates unique utility items. TAILOR (DEX + WIS): Crafts light armor, robes, cloaks, bags, and cloth items. Requires tailoring workshop. Essential for casters who can't wear heavy armor. SKILL LEVELS & EFFECTS: NOVICE (Starting): Can craft Tier 1-2 items. Base quality success rate: 70%. Craft time: Tier 1 instant, Tier 2 instant. No special bonuses. APPRENTICE (Craft 50 items OR 3 months training with Journeyman+): Can craft Tier 1-3 items. Base quality success rate: 60%. Superior chance: +5%. Craft time: Tier 1-2 instant, Tier 3 (1 day). Bonus: +5% to all quality rolls, -10% material waste on failure. Training cost: 1-3 WP. JOURNEYMAN (Craft 100 items OR 1 year training with Expert+): Can craft Tier 1-4 items. Base quality success rate: 50%. Superior chance: +10%. Craft time: Tier 1-2 instant, Tier 3 (1 day), Tier 4 (3 days). Bonus: +10% to quality rolls, -20% material waste, can modify recipes slightly. Training cost: 5-10 WP. EXPERT (Craft 75 Tier 3+ items OR 2 years training with Master): Can craft Tier 1-5 items. Base quality success rate: 40%. Superior chance: +15%, Perfect chance: +5%. Craft time: Tier 1-2 instant, Tier 3 (1 day), Tier 4 (3 days), Tier 5 (1 week). Bonus: +15% to quality rolls, -30% material waste, can create custom recipes, +1 special trait on Superior+ items. Training cost: 20-50 WP. MASTER (Craft 50 Tier 4+ items OR inherit master's legacy): Can craft Tier 1-5 items at peak efficiency. Base quality success rate: 30%. Superior chance: +20%, Perfect chance: +10%. Craft time: Tier 1-2 instant, Tier 3 (half day), Tier 4 (2 days), Tier 5 (3 days). Bonus: +20% to quality rolls, -50% material waste, can create legendary techniques, +2 special traits on Superior+ items, can craft during tribulation. Training cost: 100+ WP or inheritance only. QUALITY DETERMINATION SYSTEM: 1. Player declares crafting attempt and materials used. 2. AI determines base difficulty (Tier 1 = DC 30, Tier 2 = DC 50, Tier 3 = DC 70, Tier 4 = DC 90, Tier 5 = DC 110). 3. Player rolls: d100 + Profession Skill Bonus + Relevant Stat Modifier + Material Quality. 4. Compare result to DC: SUCCESS (meet/exceed DC): Standard quality. Roll again for Superior. SUPERIOR CHECK: d100 < Superior Chance% = Superior quality. If Superior achieved, roll for Perfect. PERFECT CHECK: d100 < Perfect Chance% = Perfect quality. FAILURE (below DC): Inferior quality (still creates item but weakened). CRITICAL FAILURE (roll 1-5): All materials destroyed, no item created. 5. AI applies quality multipliers to base effect and value. 6. AI selects appropriate special traits if Superior/Perfect. SKILL BONUSES BY LEVEL: Novice: +0 to rolls. Apprentice: +15 to rolls. Journeyman: +30 to rolls. Expert: +45 to rolls. Master: +60 to rolls. STAT BONUSES: Relevant stat (profession dependent) adds: 10-12 stat = +0, 13-15 stat = +5, 16-18 stat = +10, 19-21 stat = +15, 22+ stat = +20. FACILITY QUALITY BONUS: Basic facility (sect workshop): +0. Quality facility (personal workshop): +5. Master facility (legendary forge): +10. Tribulation crafting (Master only): +20 but extremely dangerous. LEARNING SECOND PROFESSION: Can learn second profession once first profession reaches Journeyman+. Second profession starts at Novice but advances 50% faster (requires half the items/training time). Recommended combinations: Weaponsmith + Armorer (complete equipment sets), Alchemist + Jeweler (pills + storage), Jeweler + Tailor (accessories + robes), Tailor + Alchemist (robes + pills). Poor combinations: Weaponsmith + Tailor (no synergy), Armorer + Alchemist (no overlap). PROFESSION REPUTATION: Expert+ crafters gain reputation benefits: Sect Crafter (Expert): +2 Sect Standing per month, disciples may request training, can sell to sect for guaranteed prices. Master Crafter (Master): +5 Sect Standing per month, other sects make offers, territorial lords seek services, disciples gather materials in exchange for training. Legendary Artisan (Master with 10+ Perfect items): Continental fame, Generals may target or recruit, safe passage in some territories due to value, marriage proposals from powerful clans. ABANDONING PROFESSION: Can abandon profession but lose ALL progress permanently. Cannot re-learn abandoned profession. Only consider if profession completely unsuitable or second profession vastly more successful.

## Special Traits - Superior and Perfect Quality
- Entry ID: 973
- Keywords: special traits, item properties, superior perfect traits

SPECIAL TRAITS SYSTEM: Superior and Perfect quality items gain special traits beyond base stats. Superior = 1 trait, Perfect = 2 traits. AI selects traits appropriate to item type, tier, and materials used. WEAPON TRAITS (Offensive Items): TIER 1-2 TRAITS: Keen Edge (ignore 10% of target's armor), Balanced (never miss due to poor grip), Lightweight (faster attack speed), Hardened (never breaks in combat), Scorching (minor fire damage on hit), Chilling (minor slow effect on hit). TIER 3-4 TRAITS: Vampiric (heal 10% of damage dealt), Phase Strike (ignore 25% armor), Thunderous (chain lightning to nearby enemies), Phantom Edge (attacks ignore non-magical defenses), Soul Wound (damage cannot be healed for 1 hour), Resonant (grows stronger the longer it's wielded). TIER 5 TRAITS: Reality Cleave (cut through space itself, teleport attack), Tribulation Edge (weapon survived tribulation, can harm Void+ realm), Technique Vessel (weapon can store and release cultivator's techniques independently), Heaven's Judgment (deal true damage ignoring all defenses), Ego Weapon (weapon is semi-sentient, can fight independently for short periods). ARMOR TRAITS (Defensive Items): TIER 1-2 TRAITS: Self-Repairing (slowly mends damage overnight), Lightweight (no movement penalty despite protection), Padded (reduce fall damage), Weatherproof (immune to environmental damage), Comfortable (can sleep in armor without penalty). TIER 3-4 TRAITS: Adaptive (armor shifts to protect against attack type), Qi-Reactive (converts incoming qi attacks to armor's qi), Reflection (10% chance to reflect techniques back at attacker), Regenerative (wearer heals 5 HP/hour), Fortified Mind (+20% mental resistance), Phase (30% chance attack passes through without contact). TIER 5 TRAITS: Tribulation Armor (survived tribulation, protects from Heavenly Tribulation damage), Immortal Shell (wearer cannot die while above 1 HP for 1 minute, once per day), Domain Anchor (armor creates mini-domain around wearer), Absolute Defense (one attack per day is completely negated regardless of power), Resurrection Ward (if wearer dies, armor preserves body for 7 days allowing revival). PILL/POTION TRAITS (Consumables): TIER 1-2 TRAITS: Purified (no impurities, no side effects), Long-lasting (effects last 2x duration), Fast-acting (effects immediate instead of gradual), Mild (safe for realm below target), Pleasant (tastes good instead of bitter). TIER 3-4 TRAITS: Enhanced Absorption (2x effectiveness), Stackable (can take multiple without conflict), Breakthrough Catalyst (increases next breakthrough attempt success +5%), Dual-Effect (pill provides secondary benefit), Permanent (small permanent stat increase instead of temporary). TIER 5 TRAITS: Perfect Refinement (3x effectiveness, zero impurities), Tribulation Resistance (grants temporary tribulation resistance), Bloodline Catalyst (can trigger bloodline evolution with repeated use), Age Reversal (reduces apparent age 10 years per pill), Enlightenment (grants cultivation insight, advances technique mastery). TALISMAN TRAITS (Single-use Items): TIER 1-2 TRAITS: Multi-Use (2 uses instead of 1), Quick Activation (instant instead of 1 action), Silent (no visible activation), Throwable (can affect distant target), Subtle (target unaware of talisman use). TIER 3-4 TRAITS: Rechargeable (refills with qi over 24 hours), Remote Trigger (activate from any distance), Chain Effect (affects multiple targets), Amplified (2x normal technique power), Persistent (effect lasts 10x normal duration). TIER 5 TRAITS: Technique Transcription (permanently learn technique stored in talisman), Ultimate Release (technique at Sovereign-level power regardless of user realm), Sacrifice Protection (automatically activates when wearer would die, consuming talisman), Reality Anchor (create zone where techniques of lower tier cannot function). ARRAY/FORMATION TRAITS (Placed Items): TIER 1-2 TRAITS: Mobile (can be moved after placement), Efficient (uses half normal qi upkeep), Large Area (2x normal coverage), Hidden (invisible to realm below tier), Quick Setup (deploy in 1 minute instead of 1 hour). TIER 3-4 TRAITS: Self-Powering (draws ambient qi, no maintenance needed), Adaptive (changes function based on threat), Layered (contains backup formation if primary broken), Suppression (weakens enemies inside by 1 realm), Amplification (strengthens allies inside by 20%). TIER 5 TRAITS: Eternal (never degrades, lasts centuries), Spatial Lock (prevents teleportation in/out), Time Dilation (time flows differently inside, 1 day outside = 10 days inside), Heaven's Ban (techniques of specific type cannot be used inside regardless of power), Continental (array covers entire region, affects thousands of kilometers). GENERAL PERFECT TRAITS (Any Item Type): Masterwork (all stats increased by additional 20%), Named Item (item gains legendary reputation, wielder gains fame), Bound (item bonds to creator/first user, returns when summoned, unusable by others), Eternal (never degrades regardless of use), Technique Integration (item contains cultivation technique that can be learned by extended use), Heaven's Favor (item is favored by Heavenly Dao, grants luck bonus to wielder). TRAIT SELECTION RULES: AI selects traits that make narrative sense for item's materials and purpose. Fire-based materials -> Scorching/Phoenix traits. Shadow-based materials -> Phase/Phantom traits. Dragon materials -> Ego/Resonant traits. Multiple special materials -> can blend traits (Dragon Blood + Phoenix Feather = Resurrection + Vampiric). Player can request specific trait if it makes sense for materials used, but AI has final say on appropriateness.

## Example Recipes - Famous Crafting Templates
- Entry ID: 974
- Keywords: example recipes, famous items, crafting examples

EXAMPLE RECIPES: These are famous items that exist in the world and can guide AI generation. These are NOT mandatory recipes but examples of proper formatting. IRON BODY PILL (Tier 2 Alchemist): Materials: 3 Silver Leaf (Tier 2) + 2 Golden Flower (Tier 2) + 1 Iron realm beast core (Tier 2) + 1 Earth Essence (Tier 2). Effect (Standard): +20% Body cultivation speed for 24 hours, +10% physical defense during effect. Value: 2 WP. Famous Version: 'Master Chen's Iron Body Pill' (Perfect). Effect: +40% Body cultivation speed for 48 hours, +20% physical defense, +5 permanent CON (once per realm). Special Traits: Purified (no side effects), Enhanced Absorption (double effectiveness on first use). Value: 4 WP. Story: Master Chen was Journeyman alchemist who achieved Perfect quality through 1000 attempts. His technique became sect treasure. SPIRIT IRON BLADE (Tier 2 Weaponsmith): Materials: 3 Spirit Iron (Tier 2) + 1 Fire Essence (Tier 2) + 1 Ironwood (Tier 2, handle). Effect (Standard): +20% damage, +10% qi channeling, fire-aspected. Value: 2 WP. Famous Version: 'Scorching Fang' (Superior). Effect: +30% damage, +15% qi channeling, fire-aspected. Special Trait: Scorching (inflicts burning damage over time on hit). Value: 3 WP. Story: Common weapon type elevated by Superior crafting. Many inner disciples wield versions of this blade. PHOENIX FEATHER ROBES (Tier 3 Tailor): Materials: 6 Phoenix Down (Tier 3) + 3 Celestial Silk (Tier 3) + 2 Blazing Heart (Tier 3). Effect (Standard): +30 DEF, +30% fire damage for techniques, +20% qi channeling, +40% fire resistance. Light armor (no movement penalty). Value: 3 WP. Famous Version: 'Immortal Phoenix Mantle' (Perfect). Effect: +60 DEF, +60% fire damage, +40% qi channeling, +80% fire resistance, phoenix rebirth (survive fatal blow once per day). Special Traits: Self-Repairing (mends overnight), Lightweight (weighs nothing despite protection). Value: 6 WP. Story: Core disciples of Blazing Heart Sect all aspire to wear these robes. Only sect Master can craft Perfect versions. BREAKTHROUGH PILL (Bronze->Iron) (Tier 2 Alchemist): Materials: 5 Celestial Herb (Tier 2) + 3 Phoenix Feather Grass (Tier 2) + 1 Iron beast core (Tier 2) + 1 Heavenly Dew (Tier 2). Effect (Standard): +20% tribulation success for Bronze->Iron breakthrough. One-time use. Value: 2 WP. Famous Version: 'Dao Foundation Pill' (Superior). Effect: +30% tribulation success, +5% permanent cultivation speed if breakthrough successful. Special Trait: Purified (zero impurities, no qi deviation risk). Value: 3 WP. Story: This pill recipe is closely guarded sect secret. Outer disciples who perform exceptional service may receive one. DRAGON'S FANG SWORD (Tier 4 Weaponsmith): Materials: 5 Mithril (Tier 4) + 2 Dragon Blood (Tier 4) + 1 Gold realm beast core (Tier 4) + 1 Phoenix Flame Core (Tier 4). Effect (Standard): +40% damage, +40% qi channeling, dragon's breath attack (cone of fire, 3 uses per day, recharges at dawn). Gold+ realm required. Value: 4 WP. Famous Version: 'Heaven-Rending Dragon Fang' (Perfect). Effect: +80% damage, +80% qi channeling, dragon's breath (unlimited uses, more powerful), dragon scales (grants +20 DEF when active). Special Traits: Ego Weapon (sword has draconic personality, can fight independently for 1 minute), Resonant (grows stronger with prolonged bonding, max +20% additional damage after 1 year). Value: 8 WP. Story: Only 3 known Perfect Dragon's Fang swords exist. One wielded by Righteous Blade sect leader, one sealed in Sovereign inheritance, one location unknown. SPATIAL RING (Tier 3 Jeweler): Materials: 4 Obsidian (Tier 3) + 3 Void Lotus (Tier 3) + 2 Space-Bending Thread (Tier 3) + 1 Formation Ink (Tier 3). Effect (Standard): 50 inventory slots, weightless storage. Requires formation knowledge to craft. Silver+ realm required. Value: 3 WP. Famous Version: 'Infinite Horizon Ring' (Superior). Effect: 75 inventory slots, weightless storage, time stasis inside (items never decay). Special Trait: Bound (only bonded user can access, automatically returns to user if separated). Value: 4.5 WP. Story: Essential item for any serious cultivator. Most Silver+ cultivators possess at least Standard version. Superior versions are status symbols. VOID CLOAK (Tier 4 Tailor): Materials: 6 Void Weave (Tier 4) + 4 Abyssal Dark (Tier 4) + 2 Astral beast core (Tier 4) + 2 Space-Bending Thread (Tier 4). Effect (Standard): +40 DEF, +40% stealth, can turn invisible 3 times per day (5 minutes each), +40% shadow techniques. Gold+ realm required. Value: 4 WP. Famous Version: 'Sovereign's Shadow' (Perfect). Effect: +80 DEF, +80% stealth, perfect invisibility (unlimited duration until attack), phase through walls 5 times per day, +80% shadow techniques. Special Traits: Adaptive (armor shifts to protect vital organs automatically), Ego Cloak (cloak can extend and attack independently). Value: 8 WP. Story: Worn by Sister Elowen, General of Envy. She crafted it herself before corruption. Legends say she could walk through sealed vaults unseen. TRIBULATION RESISTANCE PILL (Tier 4 Alchemist): Materials: 8 Nine Transformation Herb (Tier 4) + 5 Heaven's Blessing Flower (Tier 4) + 2 Gold realm beast core (Tier 4) + 2 Tribulation Ash (Tier 3). Effect (Standard): +30% tribulation resistance for next breakthrough attempt. Take 1 hour before tribulation begins. Gold->Astral breakthrough recommended. Value: 4 WP. Famous Version: 'Heaven-Defying Pill' (Perfect). Effect: +60% tribulation resistance, +20% permanent tribulation resistance (stacks up to 3 pills = 60% total), if tribulation survived grants bonus cultivation insight. Special Traits: Breakthrough Catalyst (+10% all future breakthrough attempts), Permanent (part of effect never fades). Value: 8 WP. Story: Only Master alchemists can craft this. Recipe requires inheritance access. Many Gold cultivators spend decades searching for just one Standard version. SOVEREIGN'S SEAL RING (Tier 5 Jeweler): Materials: 8 Eternal Steel (Tier 5) + 4 Sovereign Flame (Tier 5) + 2 Void realm beast core (Tier 4) + 2 Primordial Essence (Tier 5). Effect (Standard): +50 all stats, +100% qi pool, realm suppression (intimidate all 2+ realms below), mark of authority (recognized as Sovereign's heir/disciple). Astral+ realm required. Value: 5 WP (actually priceless, no one sells these). Famous Version: 'King Titan's Legacy Ring' (Perfect). Effect: +100 all stats, +200% qi pool, realm suppression (intimidate all 3+ realms below, stun effect on 4+ below), mark of Sovereign, bloodline resonance (enhances bloodline abilities 50%), Domain amplification (Domain 50% stronger). Special Traits: Eternal (never degrades), Bound (returns when summoned, unusable by others except bloodline descendants). Value: Priceless. Story: One of the Eight Sovereign Treasures. Worn by King Titan before his death. Now worn by MC (protagonist) as inherited birthright. HOW TO USE EXAMPLES: These examples show proper formatting for AI to follow. When player crafts similar items, AI can reference these for guidance on effects, traits, and values. AI should NOT require exact materials - these are templates, not rigid recipes. If player says 'I want to make something like Phoenix Feather Robes but with ice instead of fire,' AI adapts template: Ice Phoenix Robes using Frost materials with cold damage and ice resistance instead.

## Crafting Economics - Material Acquisition
- Entry ID: 975
- Keywords: crafting economics, gathering vs buying, material supply

CRAFTING ECONOMICS: Understanding when to gather vs purchase materials is crucial for profitable crafting. MATERIAL COSTS BY TIER: Tier 1: 0.1-0.5 WP each (very cheap, buying is fine). Tier 2: 0.5-2 WP each (moderate, buying reduces profit but still viable). Tier 3: 2-5 WP each (expensive, buying makes crafting barely profitable). Tier 4: 5-15 WP each (very expensive, buying often results in loss). Tier 5: 15+ WP each (priceless, cannot buy, must gather from inheritance sites). PROFITABILITY BY TIER: TIER 1-2 CRAFTING (Novice-Apprentice): Buying all materials: Still profitable. Profit margin 50-200%. Typical profit: 0.5-2 WP per item. Strategy: Buy materials, craft, sell to merchants or sect. Safe and steady income for beginners. Example: Buy Tier 2 materials for 4 WP total, craft Standard sword worth 2 WP, lose money. But if craft Superior (60% with Apprentice skill), worth 3 WP, small profit. Low risk, low reward. TIER 3 CRAFTING (Journeyman): Buying all materials: Barely profitable or break-even. Profit margin 0-50%. Typical profit: 0-2 WP per item (only if Superior+ quality). Strategy: Mix gathering and buying. Gather common components (herbs, beast parts from hunts), buy rare catalysts (Heavenly Dew, Tribulation Ash). Moderate effort, moderate profit. Example: Gather 6 Phoenix Down + 3 Celestial Silk (free, from quests), buy 2 Blazing Heart (6-10 WP). Craft Phoenix Robes, value 3 WP if Standard (loss!), 4.5 WP if Superior (break-even!). Must achieve Superior or better for profit. TIER 4 CRAFTING (Expert): Buying all materials: Always unprofitable. Materials cost more than finished product market value. Only profitable if materials gathered or provided by sect. Strategy: Must gather 80%+ of materials personally or have sect stipend. Hunt Astral+ beasts for cores, explore ruins for rare ores, commission disciples to gather herbs. High effort, high profit IF successful. Example: Buy Tier 4 materials (30-80 WP total), craft sword worth 4 WP Standard / 8 WP Perfect. Massive loss unless Perfect. Gather materials (free except time/danger), craft sword worth 4-8 WP, pure profit. This is why Expert crafters are rare and valuable. TIER 5 CRAFTING (Master): Buying materials: Impossible. Tier 5 materials not sold on market. Must obtain from Sovereign inheritance, defeating Generals, world-changing events, or tribulation rewards. Strategy: Only craft when materials obtained through story/inheritance. Single Tier 5 item can be priceless. Ultra-high effort, potentially priceless reward. Example: Cannot buy Sovereign Flame or Primordial Essence. Must inherit from Sovereign parent, loot from dead General, find in sealed vault, or receive as Heavenly reward. Craft Sovereign ring worth 5 WP officially but actually priceless (no one sells these). MATERIAL GATHERING STRATEGIES: OPPORTUNISTIC GATHERING (Beginner-Friendly): While questing/exploring, collect materials from defeated beasts and discovered locations. Costs no extra time, materials are 'free' bonus. Tier 1-2 materials found commonly. Store extras for future crafting or sell for WP. DEDICATED HUNTING (Intermediate): Specifically hunt beasts for desired materials (cores, pelts, blood, bones). Time-intensive but guarantees specific materials. Tier 2-3 materials from Silver-Gold realm beasts. Requires combat ability matching beast tier. Risk of injury or death. INHERITANCE EXPLORATION (Advanced): Seek out ancient ruins, Sovereign tombs, sealed vaults for rare materials. Extremely dangerous, requires puzzle-solving and combat. Tier 3-5 materials found in inheritance sites. Often one-time opportunities - return visits find sites looted. SECT STIPEND (Sect-Affiliated): Sect provides monthly material stipend to valuable crafters. Allows profitable Tier 4 crafting using sect resources. In exchange, crafter provides items for sect use (pills for disciples, equipment for elders, arrays for defense). Expert+ crafters receive 5-20 WP worth of materials monthly. Master crafters receive 20-50 WP monthly + disciples gather materials. DISCIPLE GATHERING (Master Crafters): Take disciples who gather materials in exchange for crafting training. Disciples adventure, hunt beasts, explore ruins, bring materials to master. Master crafts items, teaches techniques, disciples learn profession. Symbiotic relationship - disciples get training, master gets free materials. CO-OP POOLING (Independent Crafters): Join crafter co-ops where members pool gathered materials. Weaponsmith contributes ores from mountain expedition, Alchemist contributes herbs from forest gathering, Jeweler contributes crystals from cave exploration. Members can requisition pooled materials for personal projects, contribute finished items to co-op treasury. Reduces individual gathering burden, ensures material diversity. MARKET DYNAMICS: SELLING CRAFTED ITEMS: Standard quality: Sells for base Tier WP value. Easy to sell, always buyers. Superior quality: Sells for 1.5x Tier value. Moderate demand, discerning buyers. Perfect quality: Sells for 2x Tier value. High demand, wealthy buyers compete. Can also auction for 2-3x value. Inferior quality: Sells for 0.5x Tier value. Hard to sell, desperate buyers only. Some refuse to buy inferior goods. COMMISSIONED CRAFTING: Customers provide materials + pay crafting fee (0.5-2 WP depending on tier and crafter reputation). Crafter makes item, customer keeps result regardless of quality. Zero material risk for crafter, guaranteed profit. Popular for Tier 4+ where material costs prohibitive. Expert crafters can demand high fees due to Superior/Perfect success rates. SECT CONTRIBUTIONS: Sect disciples can donate crafted items for sect contribution points. Conversion rate varies by sect and item quality. Typical: Tier 2 Standard = 50 contribution, Tier 3 Superior = 300 contribution, Tier 4 Perfect = 2000 contribution. Allows crafters to fund technique purchases without selling for WP. WHY MATERIAL GATHERING MATTERS: Makes Tier 3+ crafting profitable (otherwise impossible). Integrates crafting with adventure/exploration loop (not separate minigame). Gives disciples/companions value (they gather while MC crafts or vice versa). Creates resource scarcity (Tier 5 materials are truly rare and valuable). Encourages sect affiliation or co-op membership (solo crafting very difficult at high tiers). Rewards player exploration (every ruin potentially contains crafting materials). Creates emergent gameplay (hunting specific beasts for their materials, commissioning party members to gather). CRAFTING AS INVESTMENT: Early game (Bronze-Iron): Invest WP in Tier 1-2 materials, craft for small profit, build capital and skill. Mid game (Silver-Gold): Gather Tier 2-3 materials while adventuring, craft valuable items, establish reputation. Late game (Astral+): Rarely buy materials, rely on gathering/inheritance, craft priceless items, become legendary artisan. Crafting professions are long-term investments. Initial costs (training, workshop, tools) are high. Returns increase exponentially at Expert+ levels when Perfect crafts become possible. Master crafters are continental powers whose services are worth territories and alliances.

## Crafting Bonuses and Special Conditions
- Entry ID: 976
- Keywords: crafting profession, blacksmithing bonus, alchemy synergy, profession selection

RACIAL CRAFTING BONUSES: Different races have natural advantages in specific professions due to cultural traditions and physical traits. DWARVES: Weaponsmith +15% quality rolls (axes, hammers, heavy weapons). Armorer +15% quality rolls (all armor types, shields). Cultural masters of forge and metal. Can smell ore quality. ELVES: Weaponsmith +10% quality rolls (bows, light weapons). Jeweler +10% quality rolls (rings, necklaces). Tailor +10% quality rolls (silk work, robes). Long lifespan allows perfection of delicate arts. Enhanced dexterity helps precision work. ORCS: Weaponsmith +10% quality rolls (two-handed weapons, brutal weapons). Armorer +10% quality rolls (heavy armor only). Cultural emphasis on strength and endurance. Natural understanding of weapon balance despite brutality. HUMANS: All professions +5% quality rolls. Adaptable learners, no specific mastery. Can learn any profession equally well. KITSUNE: Tailor +15% quality rolls (robes, cloaks). Alchemist +10% quality rolls (illusion-related consumables). Jeweler +10% quality rolls (talismans). Natural affinity for beauty and deception translates to aesthetic crafting. NAGAS: Alchemist +15% quality rolls (poisons, venoms, water-based pills). Natural venom and aquatic nature provides insight into liquid crafting. DRAGONS: Jeweler +20% quality rolls (spatial storage, formation work). Armorer +10% quality rolls (scale armor). Innate connection to space and hoarding instinct makes spatial crafting easier. DRAGONBORN: Weaponsmith +10% quality rolls (all weapons). Alchemist +10% quality rolls (fire-based pills). Jeweler +10% quality rolls (elemental accessories). Draconic heritage provides versatility. TITANS: Armorer +15% quality rolls (heavy armor, shields). Weaponsmith +10% quality rolls (massive weapons). Sheer size and strength allows working with largest pieces. CULTIVATION PATH SYNERGIES: Crafters with specific paths gain bonuses crafting path-aligned items. FIRE PATH: Weaponsmith +10% (fire-aspected weapons). Alchemist +15% (fire pills, explosive potions). Any crafting involving Fire Essence or Phoenix materials gets bonus. EARTH PATH: Armorer +15% (heavy armor, shields). Weaponsmith +10% (heavy weapons). Any crafting involving Earth Essence or Mountain materials gets bonus. WATER PATH: Alchemist +15% (fluid pills, healing potions). Jeweler +10% (water-aligned accessories). Any crafting involving Water Essence or aquatic materials gets bonus. WIND PATH: Weaponsmith +15% (bows, light weapons). Tailor +15% (light armor, cloaks). Any crafting involving Wind Essence or aerial beast materials gets bonus. SHADOW PATH: Alchemist +15% (poisons, stealth pills). Tailor +15% (stealth cloaks, shadow robes). Any crafting involving Shadow Essence or darkness materials gets bonus. LIGHT PATH: Alchemist +15% (healing pills, purification potions). Jeweler +15% (holy accessories, light talismans). Any crafting involving Light Essence or radiant materials gets bonus. BODY PATH: Armorer +15% (all armor types). Alchemist +10% (body-enhancement pills). Any crafting involving physical enhancement gets bonus. SWORD PATH: Weaponsmith +20% (swords only, all types). Natural understanding of blade craft. Can imbue sword intent into crafted swords at Expert+. SPECIAL CRAFTING CONDITIONS: Some crafts require or benefit from specific conditions beyond materials and skill. TIME-BASED CONDITIONS: FULL MOON: Shadow-aligned items +10% quality. Lunar materials more potent. SOLAR ECLIPSE: Light/Dark fusion items +15% quality. Rare opportunity (once per year). AUSPICIOUS DATES: Breakthrough pills +10% quality if crafted on cultivation festival days. Sect calendars mark these dates. TRIBULATION TIMING: Master crafters can craft DURING their own Heavenly Tribulation. Tribulation qi infuses creation, grants Tribulation Edge/Armor trait automatically. Extremely dangerous - failure means death AND wasted materials. Only attempt if confident in tribulation survival. LOCATION-BASED CONDITIONS: ANCIENT FORGE: Tier 4+ weapons +10% quality. Legendary forges imbued with generations of crafting intent. SACRED VOLCANO: Fire-aligned items +15% quality. Primordial fire essence saturates location. SOVEREIGN INHERITANCE SITE: Any crafting +20% quality. Residual Sovereign qi assists crafting process. Can only craft here during inheritance access (limited time). SECT GRAND FORGE/LAB: +5% quality for sect members. Maintained by formations and collective qi. TRIBULATION SITE: Within 24 hours of any tribulation in area, items crafted gain +5% quality and slight tribulation resistance. PATH ALIGNMENT REQUIREMENTS: Some Tier 5 recipes require specific path alignment to craft. Phoenix-based items: Require Fire Path crafter OR Fire-aligned bloodline. Dragon-based items: Require matching element crafter (Fire Dragon needs Fire Path, Ice Dragon needs Water Path). Void-based items: Require Shadow Path crafter. Primordial-based items: Require Primordial bloodline OR Ancient+ bloodline + matching path. Refusing to respect path alignment results in automatic failure and material destruction. BLOODLINE CRAFTING RESTRICTIONS: Some Divine/Legendary recipes require minimum bloodline tier. Tier 5 items with Primordial materials: Require Ancient+ bloodline to craft. Items intended for Sovereign use: Require Noble+ bloodline to craft properly. Bloodline-specific items: Require matching bloodline (Phoenix bloodline crafter for Phoenix items). Awakened bloodline crafters can attempt these with -20% quality penalty. Mortal bloodline crafters automatically fail these crafts. COLLABORATIVE CRAFTING: Master crafters can work together on single item. Requires both crafters Expert+ in their professions. Each crafter contributes their specialization (Weaponsmith forges blade, Jeweler adds gem, Alchemist infuses qi). Final quality = average of all crafters' rolls. Final item gains traits from multiple specializations. Results in unique hybrid items impossible to solo craft. Example: Weapon-Talisman Hybrid (sword that stores techniques like talisman). Requires days of coordination and mutual respect between crafters. CORRUPTED CRAFTING: Using Sin-corrupted materials creates powerful but dangerous items. Corrupted materials same tier as base but grant Corruption alongside power. Example: Wrath Iron (Tier 2) creates weapons dealing +20% damage but wielder gains +5 Corruption per day of use. Corrupted items always Superior or Perfect quality (corruption amplifies power). Corrupted items have red/black aesthetic, pulse with Sin qi, feel wrong to hold. Orthodox sects forbid corrupted crafting. Demonic cultivators seek corrupted items. Using corrupted items marks crafter as demonic sympathizer (reputation loss, sect consequences). AI should warn player before using corrupted materials: 'The Wrath Iron pulses with murderous intent. Crafting with this will create a cursed item. Proceed?' Risk/reward decision for player. FORMATION-ASSISTED CRAFTING: Expert+ crafters can inscribe formations to assist crafting process. Requires Formation knowledge (learned separately or collaboration with formation master). Quality-Enhancement Formation: +10% quality rolls, costs 1 WP in formation materials. Time-Compression Formation: Reduce craft time by half, costs 2 WP in formation materials. Safety Formation: Prevent critical failures (material loss reduced to 25% instead of 100%), costs 3 WP. Tribulation-Resistance Formation: Can craft during tribulation more safely, costs 5 WP, still very dangerous. Formations single-use, consumed during crafting process. High-end crafters maintain permanent formations in their workshops (+5% quality, always active).

## Transcendence System - Stat Overflow Solution
- Entry ID: 977
- Keywords: transcendence, overflow, stat overflow, transcendence points, TP

TRANSCENDENCE SYSTEM: When a stat reaches its realm cap (100 at Astral+), additional stat points become TRANSCENDENCE POINTS (TP). These represent power beyond mortal limits. WHEN OVERFLOW OCCURS: At Astral+ realms, stat caps are 100. Any stat point that would raise a stat above 100 instead converts to 1 TP. Players manually allocate TP into Transcendent Stats during level-up or rest. TRANSCENDENCE POINT GENERATION: Points per level above cap become TP. Example: Astral cultivator with all stats at 100 gains 5 PPL, all 5 become TP. By Sovereign 100, a player may accumulate 2,000-3,000 TP depending on build efficiency. ALLOCATION: Manual choice during level-up or long rest. Once allocated, TP cannot be reallocated without special circumstances (Sovereign-tier reforging, near-death epiphany, certain inheritance sites). AI should prompt player: 'You have X unspent Transcendence Points. Which Transcendent Stat would you like to invest in?'

## Transcendent Stats - Categories and Effects
- Entry ID: 978
- Keywords: transcendence, transcendent, transcendent stats, TP allocation, transcendence points, domain power, intent potency

TRANSCENDENT STATS: Six stats that absorb overflow power. DOMAIN POWER (Astral+ only): Cost 10 TP per point. Effect: +1% domain strength and size per point. Cap: 100 (doubles domain strength at cap). Primary stat for high-realm combat dominance. INTENT POTENCY (Astral+ only): Cost 10 TP per point. Effect: +1% technique damage per point. Cap: 100. Affects all technique damage, stacks with other bonuses. QI EFFICIENCY (Silver+ only): Cost 5 TP per point. Effect: -1% technique Qi cost per point. Cap: 50 (half-cost techniques at cap). Critical for sustained combat and attrition fights. TRIBULATION RESISTANCE (Iron+ only): Cost 5 TP per point. Effect: +1 to breakthrough tribulation rolls per point. Cap: 50. Safety net for breakthrough attempts. SOUL FORTITUDE (Astral+ only): Cost 15 TP per point. Effect: +2% corruption resistance, +1 to mental defense rolls per point. Cap: 50. Anti-corruption and anti-mind-control build. VITAL RESERVOIR (Gold+ only): Cost 10 TP per point. Effect: +5 max HP and +3 max Stamina per point. Cap: 100. Tank and endurance build.

## Transcendence Builds - Strategic Allocation
- Entry ID: 979
- Keywords: transcendence builds, TP allocation, overflow builds

TRANSCENDENCE BUILD ARCHETYPES: Players should consider their playstyle when allocating TP. DOMAIN MASTER: Focus Domain Power (100) + Intent Potency (50). Total: 1,500 TP. Result: Domain strength doubled, +50% technique damage. Best for: Solo combat, dueling Generals, battlefield control. ETERNAL WARRIOR: Focus Vital Reservoir (100) + Qi Efficiency (50). Total: 1,250 TP. Result: +500 HP, +300 Stamina, half-cost techniques. Best for: Attrition fights, protecting allies, long dungeon runs. UNCORRUPTIBLE: Focus Soul Fortitude (50) + Tribulation Resistance (50). Total: 1,000 TP. Result: +100% corruption resistance, +50 to breakthroughs, +50 mental defense. Best for: Anti-Sin General builds, corruption-heavy campaigns, safe progression. BALANCED SOVEREIGN: Spread across all stats (30-40 each). Total: ~2,500 TP. Result: Good at everything, master of nothing. Best for: Flexible players, unknown challenges. GLASS CANNON: Max Intent Potency (100) + Domain Power (100). Total: 2,000 TP. Result: +100% technique damage, doubled domain. Best for: Alpha strike builds, assassination, one-shot victories. AI GUIDANCE: When player asks for advice, consider their path, bloodline, and campaign focus. Fire/Shadow paths benefit from Intent Potency. Body path benefits from Vital Reservoir. Light path benefits from Soul Fortitude.

## Enemy Transcendence - General Domain Power
- Entry ID: 980
- Keywords: general domain power, general transcendence, enemy transcendence

ENEMY TRANSCENDENCE: Powerful enemies also accumulate Transcendent Stats over their long lives. Sin Generals have had 3,000+ years to develop. GENERAL DOMAIN POWER BONUSES: Vaelen (Pride) = +100 Domain Power (3,000 years of perfection, Eternal realm). Final Domain: 39.0 x 2.0 = 78.0. Aurex (Greed) = +80 Domain Power (obsessive accumulation). Final Domain: 26.0 x 1.8 = 46.8. Vespera (Temptation) = +60 Domain Power (calculated growth). Final Domain: 17.3 x 1.6 = 27.7. Elowen (Envy) = +30 Domain Power (youngest, only 500 years). Final Domain: 8.0 x 1.3 = 10.4. Glut (Gluttony) = +50 Domain Power (consumed much power). Final Domain: 6.0 x 1.5 = 9.0. Calderon (Wrath) = +40 Domain Power (rage-fueled but unfocused). Final Domain: 6.0 x 1.4 = 8.4. Morvane (Sloth) = +0 Domain Power (too lazy to invest). Final Domain: 1.5. BALANCE RESULT: A Sovereign MC with +100 Domain Power (36.0 total) can crush weaker Generals, challenge Vespera/Aurex, but still gets suppressed by Vaelen. This preserves endgame challenge while rewarding player investment. OTHER ENEMIES: Sect Patriarchs (Eternal) typically have +30 to +50 Domain Power. Elder cultivators (Void+) typically have +10 to +30. Random Astral enemies rarely have any TP investment.

## Transcendence Quick Reference
- Entry ID: 981
- Keywords: transcendence quick reference, TP quick reference, overflow quick

TRANSCENDENCE QUICK REFERENCE: CONVERSION: 1 overflow stat point = 1 TP. STAT COSTS: Domain Power 10:1, Intent Potency 10:1, Vital Reservoir 10:1, Qi Efficiency 5:1, Tribulation Resistance 5:1, Soul Fortitude 15:1. CAPS: Domain Power 100, Intent Potency 100, Vital Reservoir 100, Qi Efficiency 50, Tribulation Resistance 50, Soul Fortitude 50. UNLOCK REALMS: Domain Power (Astral), Intent Potency (Astral), Soul Fortitude (Astral), Vital Reservoir (Gold), Qi Efficiency (Silver), Tribulation Resistance (Iron). EXPECTED TP BY REALM: Astral 100 = ~770 TP. Void 100 = ~1,370 TP. Eternal 100 = ~2,070 TP. Sovereign 100 = ~2,870 TP. ALLOCATION: Manual during level-up or long rest. Prompt player when TP available. Cannot reallocate without special circumstances.

## Character Perks System - Overview & Acquisition
- Entry ID: 982
- Keywords: perk, perks, character perk, earned bonus, permanent bonus, achievement, unlock

CHARACTER PERKS SYSTEM:

Perks are PERMANENT bonuses earned through gameplay achievements, story milestones, and character development. Unlike equipment (removable) or bloodline abilities (inherited), perks represent growth from EXPERIENCES.

PERK ACQUISITION SOURCES:
1. BACKGROUND PERKS (1-2 from character creation Stage 6)
2. MILESTONE PERKS (earned at major story achievements)
3. TRAINING PERKS (earned through dedicated practice/study)
4. SURVIVAL PERKS (earned from surviving dangerous situations)
5. SOCIAL PERKS (earned through relationship development)
6. CORRUPTION PERKS (earned by accepting demon bargains - dark but powerful)

PERK LIMITS:
- Characters can have maximum 10 active perks
- If acquiring 11th perk, must choose one to become 'dormant' (inactive)
- Dormant perks can be reactivated by making another dormant
- Corruption perks count toward limit but cannot be made dormant once acquired

PERK TIERS:
- MINOR: Small passive bonus (+1 to checks, 5% efficiency increase)
- MAJOR: Significant bonus (+3 to checks, new capability, 15% boost)
- LEGENDARY: Rare, powerful (unique ability, major stat interaction)

AI INSTRUCTION: Award perks narratively at meaningful moments. Don't give perks for trivial actions. A perk should feel EARNED. When awarding, state: 'PERK ACQUIRED: [Name] - [Effect]'

See Entry 851 (Combat Perks), Entry 852 (Social/Utility Perks), Entry 853 (Cultivation Perks).

## Character Perks - Combat Category
- Entry ID: 983
- Keywords: combat perk, battle perk, fighting bonus, warrior perk

COMBAT PERKS (Earned through battle achievements):

MINOR COMBAT PERKS:
? Bloodied Veteran: +1 to attack rolls after taking damage
? Quick Draw: +2 initiative in first combat round
? Armored Stride: No movement penalty from heavy armor
? Off-Hand Training: -2 penalty instead of -4 for dual-wielding
? Archer's Eye: +1 to ranged attacks beyond 30 feet
? Shield Bash: Can attack with shield as bonus action (1d4 damage)
? Relentless: Stay conscious at 0 HP for 1 more round once per day
? Weapon Specialist [Type]: +1 damage with chosen weapon type
? Combat Instincts: Cannot be surprised while conscious

MAJOR COMBAT PERKS:
? First Blood: +1d6 damage on first attack against undamaged enemy
? Riposte Master: Counter-attack on missed melee attacks against you
? Adrenaline Surge: Once per combat, take extra action at cost of 10% HP
? Executioner: +50% damage against enemies below 25% HP
? Iron Will: Advantage on saves vs fear, charm, mind control
? Vital Strike: Critical hits deal triple damage instead of double
? Battle Trance: +2 to all combat stats while below 50% HP
? Pack Tactics: +2 to hit when ally is adjacent to target

LEGENDARY COMBAT PERKS (Very Rare):
? Deathless Fury: Once per day, survive fatal blow with 1 HP
? Apex Predator: +1 to all combat rolls per realm above enemy (max +5)
? Perfect Defense: Once per combat, negate any single attack completely
? One With The Blade: Weapon cannot be disarmed, +3 damage with bonded weapon

ACQUISITION EXAMPLES:
- Survive 5 near-death combat situations ? Relentless
- Kill enemy 2+ realms higher ? Apex Predator
- Win duel against rival without taking damage ? Perfect Defense
- Train with weapon master for extended period ? Weapon Specialist

See Entry 850 (Perk Overview), Entry 597 (Base Combat System).

## Character Perks - Social & Utility Category
- Entry ID: 984
- Keywords: social perk, utility perk, charisma perk, exploration perk, non-combat perk

SOCIAL & UTILITY PERKS:

MINOR SOCIAL PERKS:
? Silver Tongue: +2 to persuasion and haggling checks
? Intimidating Presence: +2 to intimidation, enemies hesitate first round
? Noble Bearing: NPCs assume higher social status, +1 to formal interactions
? Street Rat: +2 to gathering rumors, finding black markets
? Empathic Reader: Sense surface emotions, +2 to insight checks
? Linguist: Learn new languages twice as fast
? Forgettable Face: NPCs struggle to remember you, +2 to blending in
? Honest Face: +2 to deception when telling partial truths

MAJOR SOCIAL PERKS:
? Inspiring Leader: Allies gain +2 morale bonus when you give speeches
? Debt Collector: NPCs remember favors owed, can call them in reliably
? Reputation [Type]: Famous/Infamous for specific deed, affects NPC reactions
? Network: Have contacts in most major cities, can request information
? Faction Friend [Faction]: +10 starting reputation with chosen faction
? Diplomat's Immunity: Reduced hostility from enemies during parley
? Master Negotiator: Merchants give 15% better prices, contracts favor you

MINOR UTILITY PERKS:
? Light Sleeper: Wake at slightest disturbance, cannot be ambushed while resting
? Efficient Packer: Carry 25% more weight without penalty
? Direction Sense: Cannot get lost, always know cardinal directions
? Weather Reader: Predict weather 24 hours ahead accurately
? Trap Sense: +3 to detecting traps and hidden mechanisms
? Quick Learner: 10% faster skill/technique advancement
? Iron Stomach: Immune to food poisoning, can eat anything
? Night Owl: No penalties for darkness, reduced sleep needs

MAJOR UTILITY PERKS:
? Survivor: Halve environmental damage (cold, heat, poison areas)
? Lucky Find: Increased chance of finding hidden treasures and secret areas
? Spirit Touched: Can sense supernatural presence within 30 feet
? Beast Friend: Animals are not naturally hostile, easier to tame
? Treasure Hunter: Automatically detect valuable items in searched areas
? Jack of All Trades: +1 to all skills you have no training in

LEGENDARY UTILITY PERKS:
? Fate's Favorite: Once per session, reroll any failed check
? Merchant Prince: Access to black market, rare items, 25% discount
? Spymaster: Information network spans realm, can discover secrets remotely

ACQUISITION EXAMPLES:
- Broker peace between warring factions ? Diplomat's Immunity
- Survive alone in wilderness for extended time ? Survivor
- Build genuine friendships with 5+ NPCs ? Network

See Entry 850 (Perk Overview), Entry 853 (Cultivation Perks).

## Character Perks - Cultivation & Corruption Category
- Entry ID: 985
- Keywords: cultivation perk, qi perk, breakthrough perk, path perk, realm perk

CULTIVATION PERKS (Earned through cultivation achievements):

MINOR CULTIVATION PERKS:
? Efficient Meridians: 10% reduced Qi cost for techniques
? Meditation Focus: +2 to cultivation session effectiveness
? Qi Sense: Detect cultivator realm within 20 feet passively
? Stable Foundation: +1 to breakthrough checks
? Recovery Breathing: Restore 5% Qi during short rests
? Elemental Affinity [Element]: +1 damage with aligned techniques
? Technique Memory: Learn techniques 15% faster

MAJOR CULTIVATION PERKS:
? Perfect Core: +10% max Qi pool permanently
? Hardened Spirit: +3 to resist corruption from demon influence
? Dual Harmony: No penalty for practicing two cultivation paths
? Bloodline Resonance: Bloodline abilities cost 20% less Qi
? Enlightened Mind: Comprehend technique scrolls one tier higher
? Qi Overflow: When at max Qi, techniques deal +15% damage
? Foundation of Stone: Cannot be knocked below current realm by corruption
? Accelerated Recovery: Heal injuries 25% faster, reduce recovery time

LEGENDARY CULTIVATION PERKS:
? Heavenly Constitution: +1 to all stats permanently
? Dao Heart: Immune to Heart Demons, +5 to all willpower saves
? Bloodline Awakening: Unlock dormant bloodline ability (DM determines)
? Perfect Breakthrough: Next realm advancement has no failure chance
? Technique Fusion: Can combine two known techniques into hybrid form

CORRUPTION PERKS (Dark - Accepted from demon bargains):

?? WARNING: Corruption perks are powerful but have hidden costs.

? Demon's Vitality: +25% max HP, but healing from holy sources halved
? Infernal Strength: +5 STR, but take +10% damage from blessed weapons
? Whispered Secrets: Hear demon communications, gain intel, but sanity checks
? Shadow Step: Short-range teleport through shadows, but sunlight causes pain
? Soul Siphon: Killing enemies restores HP, but mercy becomes difficult
? Dark Pact [General]: Specific boon from a Demon General, unique effect
? Corruption Mastery: Corruption cap raised to 75% before consequences

CORRUPTION PERK RULES:
- Each corruption perk adds +5% permanent corruption
- Cannot be made dormant once acquired
- Taking 3+ corruption perks triggers suspicion from sects/NPCs
- At 5+ corruption perks, considered 'touched by darkness' by detection spells

ACQUISITION EXAMPLES:
- Achieve breakthrough without assistance ? Stable Foundation
- Reach High Bronze before age 20 ? Accelerated Recovery
- Resist demon temptation at great personal cost ? Dao Heart
- Accept demon bargain for power ? Dark Pact [specific]

See Entry 850 (Perk Overview), Entry 595 (Corruption System), Entry 583 (Breakthrough System).

## Legendary Artifact: Atlas Mantle
- Entry ID: 986
- Keywords: atlas mantle, legendary artifact, body path artifact, cloak, pauldrons

Atlas Mantle [Legendary, Tier 5, Body, Astral+] - DOMAIN: 1.5x. STR cap +20 (max 120), immovable +10 CON, Atlas's Burden 1/day (take all ally dmg 20m for 5 rounds, min 1 HP), carry allies +5 stats, lift 10 tons [STR 60+ or Paralyzed, -30% move, empathy curse, compelled to aid, cannot swim]

## Legendary Artifact: Celestial Halo
- Entry ID: 987
- Keywords: celestial halo, legendary artifact, light path artifact, headpiece, amulet

Celestial Halo [Legendary, Tier 5, Light, Astral+] - DOMAIN: 1.5x. Aura 25m: allies +2 saves +10% dmg, enemies -2 saves, demons burn [WISx2]/round; Judgement Ray 1/day ([WISx8], banish Epic- demons); corruption immune, +5 all saves; death ward 1/ally/battle [+50 Notoriety floor, always visible, divine commands, moral judgment, social extremes]

## Legendary Artifact: Dawnbringer Hammer
- Entry ID: 988
- Keywords: dawnbringer hammer, legendary artifact, light path artifact, earth path artifact, war hammer, mace

Dawnbringer Hammer [Legendary, Tier 5, Light/Earth, Astral+] - DOMAIN: 1.5x. 3x dmg vs evil (5x demons, 6x wicked), Dawn's Wrath 1/day (40m burst [STRx5+WISx5] dmg + heal allies [CONx4]), blind on crit, +[STRx2] HP, corruption immune, holy ground 5m/hour [STR 50+ required, always glows, cannot harm innocents, compelled vs evil]

## Legendary Artifact: Earthshaker Gauntlets
- Entry ID: 989
- Keywords: earthshaker gauntlets, legendary artifact, earth path artifact, body path artifact, gauntlets

Earthshaker Gauntlets [Legendary, Tier 5, Earth/Body, Silver High+] - DOMAIN: 1.5x. Earthquake Punch 3/day (25m, [STRx4+CONx3]), +[STRx3] unarmed dmg, ignore 50% AC, crit 18-20, tremor sense 50m, +10 grapple [Cannot do delicate tasks, -5 CHA diplomacy, aggression compulsion]

## Legendary Artifact: Fist of the Immortal
- Entry ID: 990
- Keywords: fist of the immortal, legendary artifact, body path artifact, gauntlet

Fist of the Immortal [Legendary, Tier 5, Body, Gold+] - DOMAIN: 1.5x. +[STRx4+CONx2] unarmed dmg, bypass all armor, crit 17-20; Death Defiance resurrect 1/day + heal allies [CONx3]; Killing Fist 1/day (instant kill <25% HP or [STRx10] dmg); ageless +500 years [Cannot remove, right hand becomes gauntlet, compelled to duel, -5 stats if no realm-level combat for 7 days, inhuman hand -3 CHA contact]

## Legendary Artifact: Frozen Heart Amulet
- Entry ID: 991
- Keywords: frozen heart amulet, legendary artifact, water path artifact, ice artifact, amulet

Frozen Heart Amulet [Legendary, Tier 5, Water/Ice, Silver Mid+] - DOMAIN: 1.5x. Absolute Zero aura (-20% enemy move, fire -5 hit), ice armor regen 10/round, Frozen Time 1/day, cold immunity, corruption gain -50% [CHA -3, romance gains halved]

## Legendary Artifact: Heaven's Decree
- Entry ID: 992
- Keywords: heaven's decree, legendary artifact, sword path artifact, light path artifact, jian, straight sword

Heaven's Decree [Legendary, Tier 5, Sword/Light] - DOMAIN: 1.5x. 2x dmg vs evil (auto-crit), Purifying Light 1/day, corruption immunity, +5 AC vs dark [Cannot harm innocents]

## Legendary Artifact: Muramasa
- Entry ID: 993
- Keywords: muramasa, legendary artifact, sword path artifact, katana, cursed sword

Muramasa [Legendary Cursed, Tier 5, Sword, Astral+] - DOMAIN: 1.5x. 3x dmg vs demons/corrupted, blood healing +dmg stacks +20 max, ignore 75% AC, Killing Intent 1/battle [CURSE: Kill or shed blood every 7 days, +5% corruption every 60 days, +30 Notoriety, demonic whispers]

## Legendary Artifact: Phoenix Crown of Rebirth
- Entry ID: 994
- Keywords: phoenix crown of rebirth, legendary artifact, fire path artifact, crown, headpiece

Phoenix Crown of Rebirth [Legendary, Tier 5, Fire] - DOMAIN: 1.5x. Phoenix Rebirth 1/week, immune to fire, -15 Qi fire techniques

## Legendary Artifact: Shadowfang Dagger
- Entry ID: 995
- Keywords: shadowfang dagger, legendary artifact, shadow path artifact, dagger

Shadowfang Dagger [Legendary, Tier 5, Shadow, Gold+] - DOMAIN: 1.5x. Ignore AC/armor (shadow path 30m), Shadow Merge 3/day (5 rounds intangible), Assassination 5x dmg 1/day (unaware only), shadow teleport 30m [Nightmare curse after 10 kills, must kill monthly, -3 CHA, only works from stealth]

## Legendary Artifact: Stormcaller's Mantle
- Entry ID: 996
- Keywords: stormcaller's mantle, legendary artifact, wind path artifact, cloak, robe

Stormcaller's Mantle [Legendary, Tier 5, Wind, Gold+] - DOMAIN: 1.5x. Flight 2x speed, Thunder Storm 1/day (50m, [WISx5] lightning), Wind Step teleport 20m unlimited, +5 AC cyclone shield, lightning immune [+10 Notoriety, creates storms, cannot remove in combat]

## Legendary Artifact: Tidekeeper's Trident
- Entry ID: 997
- Keywords: tidekeeper's trident, legendary artifact, water path artifact, trident, spear

Tidekeeper's Trident [Legendary, Tier 5, Water, Silver High+] - DOMAIN: 1.5x. +3 to hit, Tidal Command 1/day, +30% water dmg/range, water breathing, crit heals [WISx2] [Daily water immersion required]

## Legendary Artifact: Titan's Aegis
- Entry ID: 998
- Keywords: titan's aegis, legendary artifact, earth path artifact, shield, tower shield

Titan's Aegis [Legendary, Tier 5, Earth, Gold+] - DOMAIN: 1.5x. Mountain Dome 1/day (30m, [CONx100] HP), immovable +10 AC frontal, Guardian Sacrifice (transfer all ally damage), +[CONx3] HP, regen [CON/2]/round on earth [STR 60+ required, compelled to protect, attracts refugees]

## Legendary Artifact: Voidweaver Robes
- Entry ID: 999
- Keywords: voidweaver robes, legendary artifact, shadow path artifact, robes

Voidweaver Robes [Legendary, Tier 5, Shadow, Gold+] - DOMAIN: 1.5x. Attackers -4 to hit, +8 AC, crit immune, Phase Shift 3/day (3 rounds intangible), 15m darkness aura (enemies Blinded), void storage 500 slots [Void-touched -3 social every 60 days, healing -50%, light vulnerable +50% dmg, 2 hrs darkness daily]

## Legendary Artifact: Worldbreaker Greatsword
- Entry ID: 1000
- Keywords: worldbreaker greatsword, legendary artifact, fire path artifact, sword path artifact, greatsword

Worldbreaker Greatsword [Legendary, Tier 5, Fire/Sword, Astral+] - DOMAIN: 1.5x. STR cap +10, Volcanic Eruption 1/day, ignore 50% armor, magma trails [+25 Notoriety, STR 40+ required]

## Legendary Artifact: Zephyr Blade
- Entry ID: 1001
- Keywords: zephyr blade, legendary artifact, wind path artifact, sword path artifact, dao, curved sword

Zephyr Blade [Legendary, Tier 5, Wind/Sword] - DOMAIN: 1.5x. DEX for dmg, 2 attacks/round, Vacuum Slash 3/day, Wind Scatter evade 3/day

## Crippled Injury Types (1d8 Table)
- Entry ID: 1002
- Keywords: crippled injuries, lost limb, damaged meridians, shattered core, blinded, soul scarred

CRIPPLED INJURY TYPES (Roll 1d8 or select narratively): 1. LOST LIMB (ARM): Cannot use two-handed weapons, -3 to physical rolls involving that arm. Healing: Eternal+ technique or legendary prosthetic only. 2. LOST LIMB (LEG): Half movement speed, cannot flee combat, -3 DEX. Healing: Eternal+ technique or legendary prosthetic only. 3. DAMAGED MERIDIANS: -30% Qi capacity, half cultivation speed, +50% technique costs. Healing: Tier 4 Rebirth Pill (3-6 months) or Tier 5 Miracle Pill (instant). 4. SHATTERED CORE: Cannot advance realms, -5 to all technique rolls. Healing: Tier 5 Miracle Pill (partial/full based on quality) or Sovereign intervention. 5. BLINDED: -8 to combat rolls, cannot read or identify visual threats. Healing: Tier 5 Miracle Pill (Superior+ for full restoration). 6. DEAFENED: -4 initiative, significant social penalties, cannot hear warnings. Healing: Tier 4 Rebirth Pill. 7. SOUL SCARRED: +20% corruption vulnerability, -3 WIL, plagued by nightmares. Healing: Tier 4 Rebirth Pill or Light Path purification. 8. DISFIGURED: -5 CHA for first impressions, psychological trauma, may trigger fear in others. Healing: Time + care (1-2 years) or Tier 3+ restoration. COMPANION DEPARTURE RISK: Crippled companions may choose to leave. CHA check to convince stay: DC = 20 - (Loyalty / 5). Success: +5 loyalty, stay. Failure: departs (tracking quest may become available).

## MC Primordial Bloodline Injury Protection
- Entry ID: 1003
- Keywords: MC injury protection, primordial injury, bloodline protection

MC PRIMORDIAL BLOODLINE PROTECTION: The protagonist's dormant Primordial bloodline provides special protection against permanent injury. CRIPPLED PROTECTION: Roll twice when determining Crippled injury, take the less severe result. Cannot suffer Shattered Core - bloodline automatically protects cultivation foundation (reroll if result is 4). RECOVERY BONUS: 1.5x recovery speed for all injury tiers (Shaken 2-3 days, Injured 5-9 days, Severely Injured 20-30 days). FULL AWAKENING HEALING: When bloodline fully awakens at Void realm breakthrough, MC can choose to heal any one Crippled condition instantly as part of the awakening. This represents the Primordial essence reconstructing the body. DEATH PROTECTION: MC has one free 'death save' per major arc - if MC would die, bloodline flares and stabilizes them at Severely Injured instead. This can only trigger once until bloodline evolves to next tier. AI NOTE: These protections exist to maintain protagonist plot armor while still making injuries meaningful. Companions do not have these protections.

## Combat Healing Usage Limits
- Entry ID: 1004
- Keywords: healing item limits, pill usage cap, combat healing limit

COMBAT HEALING USAGE LIMITS: Higher tier pills are more potent but the body can only absorb so much concentrated qi medicine. Each tier has maximum uses per battle. TIER CAPS: Tier 1 = 7 uses max, Tier 2 = 6 uses max, Tier 3 = 5 uses max, Tier 4 = 3 uses max, Tier 5 = 2 uses max. STACKING RULES: Limit applies per pill TYPE (can use 7 Tier 1 HP pills AND 7 Tier 1 Qi pills in same battle). Mixed tiers count separately (can use 2 Tier 5 HP pills AND 5 Tier 3 HP pills). Different categories stack freely (HP pill + Qi pill + Stamina pill all work at full effectiveness). EXCEEDING LIMIT: Additional pills beyond cap have no effect and are wasted. RESET: Limit resets after 1 hour of rest between combats. BREAKTHROUGH PILLS: Maximum 3 pills affecting same breakthrough attempt. Additional pills provide no benefit and may cause qi deviation.

## Injury Recovery Items
- Entry ID: 1005
- Keywords: recovery pills, injury recovery items, mending pill, restoration pill, rebirth pill, miracle pill

INJURY RECOVERY ITEMS: Pills that treat persistent injury statuses (Entry 629). Higher tiers treat more severe injuries. TIER REQUIREMENTS: Tier 1 treats Shaken (accelerate), Tier 2 cures Shaken and accelerates Injured, Tier 3 cures Injured and accelerates Severely Injured, Tier 4 cures Severely Injured and treats some Crippled, Tier 5 cures most Crippled. NAMED RECOVERY PILLS: TIER 1 CALMING PILL (1 WP) - Reduces Shaken recovery by 2 days. Superior cures immediately. TIER 2 MENDING PILL (2 WP) - Cures Shaken immediately. Reduces Injured recovery by 3 days (Superior: 5 days, Perfect: 7 days). TIER 3 RESTORATION PILL (3 WP) - Cures Injured immediately. Reduces Severely Injured recovery by 7 days (Superior: 12 days, Perfect: 18 days). TIER 4 REBIRTH PILL (4 WP) - Cures Severely Injured immediately. Begins healing Damaged Meridians, Deafened, Soul Scarred (6 months ? 3 months Standard, ? 2 months Superior, ? 1 month Perfect). TIER 5 MIRACLE PILL (5 WP) - Restores Shattered Core (partial at Standard, major at Superior, full at Perfect). Restores Blinded (Superior+ for full). Full meridian cure. Cannot restore lost limbs. DAILY LIMIT: One recovery pill per injury per day. Body must process healing qi. PERFECT EXCEPTION: Perfect quality recovery pills bypass daily limit.

## Purification Items (Corruption Reduction)
- Entry ID: 1006
- Keywords: purification items, corruption reduction, cleansing pill, purifying pill, sacred lotus, purification

PURIFICATION ITEMS: Consumables that reduce corruption. Critical for players using Sin techniques. PURIFICATION RULES: Only works below Void realm (once Void with corruption, it's permanent). Diminishing returns at high corruption. Cannot use during active corruption gain (wait 1 hour after Sin technique). PURIFICATION PILLS - Formula [5 + (Tier x 3)]% corruption reduction: TIER 1 CLEANSING PILL (1 WP) - Reduces 5% corruption. Only works below 25% corruption. TIER 2 PURIFYING PILL (2 WP) - Reduces 8% corruption. Only works below 50% corruption. TIER 3 SACRED LOTUS PILL (3 WP) - Reduces 12% corruption. Only works below 75% corruption. TIER 4 HEAVENLY CLEANSING PILL (4 WP) - Reduces 18% corruption. Works at any level below Void. TIER 5 DIVINE PURIFICATION PILL (5 WP) - Reduces 25% corruption OR halts corruption progression for 30 days. Works at any level below Void. QUALITY EFFECTS: Inferior 50% effectiveness. Standard as listed. Superior 150% effectiveness + 10% corruption resistance 24 hours. Perfect 200% effectiveness + 20% corruption resistance 7 days. SPECIAL ITEMS: Purification Incense (T2-3, -3 to -5% for whole party, 1 hour exposure). Sacred Spring Water (T3, -10% + removes Sin whisper effects). Repentance Elixir (T4, -20% but costs 20% HP, grants 48hr immunity). PATH SYNERGIES: Light Path +20%, Water Path +10% quality when crafting purification items. Shadow Path cannot craft purification items. DAILY LIMIT: One purification item per day. Perfect quality bypasses limit.

## Healer Active Treatment Mechanics
- Entry ID: 1007
- Keywords: healer treatment, active treatment, healer WIS check

HEALER ACTIVE TREATMENT: Once per day per companion, Healer can perform active treatment with WIS check. FOR SHAKEN: WIS check DC 10. Success: Remove Shaken immediately. Failure: Reduce Shaken recovery by 1 day. FOR INJURED: WIS check DC 12. Success: Reduce recovery by 3 days (stacks with passive). Failure: Reduce recovery by 1 day. FOR SEVERELY INJURED: WIS check DC 15. Success: Reduce recovery by 7 days (stacks with passive). Failure: Reduce recovery by 2 days. Critical Success (beat DC by 10+): Reduce by 14 days. FOR CRIPPLED: Healer cannot cure Crippled directly. Can provide comfort care preventing loyalty decay while under Healer's care. Can assist with high-tier items (+20% effectiveness when Healer administers). ITEM ADMINISTRATION BONUS: When Healer administers items (not self-administered): HP/Qi/Stamina Pills +20% effectiveness. Recovery Pills act as +1 tier (T2 acts as T3). Purification Pills +10% extra corruption reduction. Salves T1-3 can be applied in combat. HEALER PATH BONUSES: Water Path: +10% to all recovery reductions, can treat +1 additional companion per day. Light Path: Can treat corruption as injury (-5% corruption per daily treatment). Body Path: Treatment DCs reduced by 2, stabilization grants +2 to ALL bleedout saves.

## Healer Supplies and Loyalty
- Entry ID: 1008
- Keywords: healer supplies, medical supplies, healer loyalty

HEALER SUPPLIES: Healers require basic supplies for full effectiveness. SUPPLY LEVELS: Well-Stocked (1 WP/week): Full bonuses. Adequate (0.5 WP/week): -10% to all bonuses. Low (negligible cost): -25% to all bonuses, no item administration bonus. Depleted (no supplies): Passive only, no active treatment. RESUPPLY: Any town, sect dispensary, or herbalist. Healer can gather supplies in wilderness (WIS check DC 12, takes 2 hours). HEALER LOYALTY INTERACTIONS: GAINS: Healer saves companion from death (+5 with saved, +2 with party). Healer cures Severely Injured (+3 with healed). MC provides quality supplies/equipment (+3). MC praises Healer's work (+1). LOSSES: Companion dies while Healer present (-5, self-blame). MC ignores medical advice (-2). Party frequently takes reckless risks (-1 per major incident). Supplies run out due to MC negligence (-3). HEALER BREAK POINTS: MC deliberately prevents Healer from treating enemy/neutral party. MC uses healing supplies for non-medical purposes. MC forces non-combatant Healer to fight.

## Master Camp Event Trigger
- Entry ID: 1009
- Keywords: camp event generator, camp events, downtime event

CAMP EVENT GENERATOR:
When the party rests or spends downtime at camp, roll 1d6. On a 1-2, trigger one of the following vignettes involving BACKGROUND companions or CAMP FOLLOWERS:

1. TRAINING (XP Gain): Two companions sparring or meditating together.
2. CONFLICT (Drama): A disagreement over philosophy, resources, or past actions.
3. BONDING (Relationship): Shared meal, storytelling, or comfort.
4. DISCOVERY (Quest): A companion finds a clue or notices something strange.
5. REQUEST (Active Duty): A background companion asks to join the active party for a specific reason.
6. CAMP LIFE (Flavor): A camp follower performing their role (cooking, crafting, scouting).

INSTRUCTION: Choose companions who are NOT currently in the active party if possible. Use their Relationship Tags to color the interaction.

## Training Vignettes
- Entry ID: 1010
- Keywords: training event, sparring event

CAMP EVENT: TRAINING
Generate a brief scene of two companions training.

VARIATIONS:
- Sparring Match: Physical contest. Winner gains small XP. Loser gains respect.
- Meditation Circle: Shared cultivation. Both gain small Qi recovery.
- Technique Instruction: One teaches the other a trick. (Mentor tag applies).
- Competitive Drill: Who can break the rock faster? (Rival tag applies).

OUTCOME: Briefly describe the training, then apply a small mechanical benefit (e.g., "They both look winded but sharper. +5 Levels for background members.").

## Conflict Vignettes
- Entry ID: 1011
- Keywords: conflict event, argument event

CAMP EVENT: CONFLICT
Generate a brief scene of tension between two companions.

VARIATIONS:
- Philosophical Debate: Light vs. Shadow, Duty vs. Freedom.
- Resource Dispute: Who gets the last ration/potion?
- Past Grievance: Bringing up a past failure or slight.
- Jealousy: One feels the MC favors the other.

OUTCOME: The MC may need to intervene. If unresolved, apply a temporary [Distrust] tag between them.

## Bonding Vignettes
- Entry ID: 1012
- Keywords: bonding event, social event

CAMP EVENT: BONDING
Generate a brief scene of connection.

VARIATIONS:
- Shared Meal: Cooking together or sharing a drink.
- Storytelling: Sharing a tale from their homeland/sect.
- Comfort: One comforting the other after a hard battle.
- Hobby: Playing a game, carving wood, maintaining gear.

OUTCOME: Strengthens their bond. If they had a [Distrust] tag, remove it. If neutral, consider adding [Friendly].

## Discovery Vignettes
- Entry ID: 1013
- Keywords: discovery event, quest hook

CAMP EVENT: DISCOVERY
A companion notices something important.

VARIATIONS:
- Omen: "The stars look wrong tonight."
- Clue: "I recognize these markings from my grandfather's journal."
- Intruder: "Someone was watching the camp."
- Resource: "I found a patch of spirit herbs nearby."

OUTCOME: Provides a hook for a side quest or immediate resource gain.

## Request Vignettes
- Entry ID: 1014
- Keywords: request event, active duty request

CAMP EVENT: REQUEST
A background companion asks to join the active party.

VARIATIONS:
- Personal Stake: "The next area is related to my backstory."
- Boredom: "I'm tired of sitting around. Let me fight!"
- Strategic: "My skills are better suited for this terrain."
- Protection: "I have a bad feeling about your safety."

OUTCOME: If accepted, swap them into the active party. If refused, they may gain a temporary [Disappointed] tag or lose small Loyalty.

## Camp Life Vignettes
- Entry ID: 1015
- Keywords: camp life event, camp role event

CAMP EVENT: CAMP LIFE
A companion performs their Camp Role or daily routine.

VARIATIONS:
- Cook: Preparing a special meal with gathered ingredients.
- Spy: Decoding a message or cleaning weapons.
- Healer: Mixing salves or tending to minor wounds.
- Scholar: Reading an ancient tome by the fire.

OUTCOME: Triggers the passive buff associated with their Camp Role (Entry 2010). Adds flavor and reinforces their utility.

## Core Companion System - Framework
- Entry ID: 1016
- Keywords: companion system, party member, follower system, NPC recruitment

COMPANION SYSTEM OVERVIEW: Sinveil uses dynamic companion recruitment where MC can have 3 ACTIVE PARTY MEMBERS (combatants) and up to 6 BACKGROUND PARTY MEMBERS plus 5 CAMP FOLLOWERS (non-combatants). All companions have complete personalities, loyalty systems, memories, and personal growth. ACTIVE PARTY: Fight alongside MC in combat, gain experience, can be swapped with background party. BACKGROUND PARTY: Stay at base, train independently, available for rotation, maintain relationships with MC. CAMP FOLLOWERS: Non-combatants who provide services, have full personalities and loyalty but no combat stats. CRITICAL: Every companion must feel UNIQUE. No two companions should have identical personality combinations, speech patterns, or story arcs. AI should create varied, memorable characters that surprise players across multiple playthroughs. RECRUITMENT: Companions can be met anywhere - sect missions, random encounters, cities, rescued from demons, rival sects, even reformed enemies. MC can attempt to recruit anyone they meet if relationship is developed. DISMISSAL: Companions can leave if loyalty drops too low, if MC betrays them, or if story requires. Some departures are permanent, others allow reconciliation.

## Universal Companion Template - All NPCs
- Entry ID: 1017
- Keywords: generate companion NPC, create new companion, companion personality, romance potential

COMPANION CHARACTER TEMPLATE: Every recruited companion (party member or camp follower) uses this framework. IDENTITY: Name, Race (from 15 playable races), Age, Gender, Cultivation Realm (current), Bloodline Tier (usually fixed), Primary Cultivation Path, Secondary Path (if any), Current Techniques Known (3-5 based on realm), Combat Role (Tank/DPS/Support/Healer/Scout) OR Camp Role (Manager/Quartermaster/Scholar/Healer/Cook/Spy/Merchant/Artisan). PERSONALITY MATRIX: Primary Trait (dominant characteristic), Secondary Trait (supporting characteristic), Flaw (weakness or vice), Virtue (strength or moral quality), Speech Pattern (how they talk), Quirk (memorable mannerism), Sense of Humor (type or none), Emotional Range (expressive/stoic/volatile). LOYALTY SYSTEM: Loyalty Score (0-100), Relationship Status (Stranger 0-20, Acquaintance 21-40, Friend 41-60, Trusted 61-80, Devoted 81-95, Sworn 96-100), Loyalty Modifiers (what increases/decreases their loyalty specifically), Betrayal Threshold (personal breaking point), Romance Potential (yes/no/conditional - gates access to Entry 580 romance stages; when relationship becomes official at COMMITTED 70+, apply [Romance: Name] tag from Entry 2011 for doubled loyalty effects). BACKGROUND: Origin Story (where from, family, past), Motivation (why they follow MC initially), Secret (hidden truth about them), Personal Quest (locked until 60+ loyalty, multi-stage arc), Fears (what terrifies them), Dreams (what they want most). RELATIONSHIPS: Opinion of MC (changes over time), Opinions of Other Companions (can form friendships/rivalries within party), Faction Loyalties (sect, clan, General if corrupted), People They Care About (leverage points), Active Relationship Tags (see Entry 2011 for [Rival], [Mentor], [Romance], [Debt], etc.). MEMORY SYSTEM: First Meeting with MC, Key Shared Experiences (victories, tragedies, promises), Inside Jokes or Bonds, Promises Made/Broken, Betrayals Witnessed, Growth Moments. PROGRESSION: Can advance cultivation realm through training/combat. Can breakthrough with MC's help. Can awaken bloodline under special circumstances. Can learn new techniques. Personality can evolve based on experiences. Loyalty shifts based on MC's actions. DEATH: Companions can die permanently in combat if MC fails to protect them. Deaths should be meaningful and affect MC and other companions. Some companions may have resurrection potential based on bloodline/story. SEE ALSO: Entry 580 (Romance Stages), Entry 2011 (Relationship Tags).

## Personality Trait Library - Primary Traits
- Entry ID: 1018
- Keywords: personality traits, character traits, NPC personality

PRIMARY PERSONALITY TRAITS (60+ options - choose ONE as dominant characteristic): POSITIVE DOMINANT: Brave (faces danger head-on), Loyal (devoted to friends/causes), Compassionate (empathetic, helps others), Wise (thoughtful, gives good advice), Cheerful (optimistic, lifts spirits), Honest (truth-teller, transparent), Disciplined (focused, controlled), Generous (shares freely), Humble (modest about abilities), Patient (tolerates frustration well), Protective (shields loved ones), Determined (unstoppable will), Charismatic (magnetic personality), Creative (innovative thinker), Reliable (always delivers), Calm (unshakable composure). NEUTRAL DOMINANT: Pragmatic (practical over idealistic), Curious (asks questions, explores), Ambitious (seeks advancement), Independent (self-reliant), Cautious (risk-averse), Competitive (driven to win), Adaptable (flexible, goes with flow), Reserved (keeps thoughts private), Logical (reason over emotion), Traditional (respects old ways), Spontaneous (impulsive decisions). NEGATIVE DOMINANT: Arrogant (overconfident, condescending), Cowardly (avoids danger), Greedy (hoards resources), Cruel (enjoys others' pain), Manipulative (uses people as tools), Paranoid (trusts no one), Reckless (danger-seeking), Cynical (expects worst), Lazy (avoids work), Jealous (envious of others), Vengeful (holds grudges), Stubborn (refuses to compromise). COMPLEX DOMINANT: Haunted (traumatized by past), Conflicted (torn between paths), Obsessed (single-minded focus), Mysterious (intentionally enigmatic), Melancholic (chronically sad), Zealous (fanatically devoted to cause), Eccentric (delightfully strange), Feral (barely civilized), Noble (bound by honor code), Jaded (seen too much), Innocent (naive about world). AI INSTRUCTION: Primary trait should be immediately obvious in first meeting. It shapes 60% of companion's actions and dialogue. Other traits add nuance but don't override primary.

## Flaw Library - Makes Characters Memorable
- Entry ID: 1019
- Keywords: character flaws, weaknesses, vices

CHARACTER FLAWS (50+ options - choose 1-2 per companion): BEHAVIORAL: Impulsive (acts before thinking), Gullible (easily deceived), Vindictive (seeks revenge disproportionately), Judgmental (harsh critic), Tactless (says wrong thing), Indecisive (can't choose), Procrastinator (delays action), Perfectionist (never satisfied), Reckless (danger-seeking), Stubborn (won't change mind), Cowardly (avoids confrontation), Aggressive (quick to violence), Passive (lets others decide), Naive (doesn't see danger), Pessimistic (expects failure). EMOTIONAL: Jealous (envious easily), Insecure (needs constant validation), Temperamental (mood swings), Bitter (resentful of past), Callous (unfeeling toward others), Anxious (constantly worried), Proud (won't admit mistakes), Self-loathing (hates self), Emotionally distant (can't connect), Clingy (fears abandonment), Volatile (explosive anger). VICES: Greedy (hoards resources, won't share), Gluttonous (overindulges food/drink), Lustful (inappropriate advances), Addicted (substances, gambling, violence), Vain (obsessed with appearance), Selfish (me-first mentality), Lazy (avoids work). SOCIAL: Distrustful (paranoid), Isolated (pushes people away), Socially awkward (can't read cues), Manipulative (uses people), Dishonest (lies habitually), Gossipy (spreads rumors), Petty (holds small grudges), Arrogant (condescending), Attention-seeking (must be center). SPECIALIZED: Bloodthirsty (enjoys killing), Haunted by guilt, Phobia (specific fear that cripples), Secret keeper (lies about past), Cursed (magical affliction), Oath-bound (restrictive vow), Split personality (two personas), Corrupted (fighting demon influence), Suicidal ideation (death wish). AI INSTRUCTION: Flaws should create complications and drama. MC should sometimes need to work around companion's flaw or help them overcome it. Flaws can evolve - jealous companion learns trust, coward finds courage. But change should be gradual and earned through story beats.

## Secret Library - Reveals at 60+ Loyalty
- Entry ID: 1020
- Keywords: companion secrets, hidden truths, plot twists

COMPANION SECRETS (30+ options - revealed at 60+ loyalty or dramatically): IDENTITY SECRETS: Actually noble/royalty in hiding. Real name is different (fled from something). Different race than appears (glamour/disguise). Actually much older than looks (immortal/de-aged). Fake cultivation realm (hiding power or weakness). Related to famous/infamous figure. Illegitimate child of Sovereign/General. PAST SECRETS: Murdered someone (justified or not). Betrayed previous master/sect. Failed to save loved one. Was corrupted, then purified. Former General cultist seeking redemption. Participated in massacre/war crime. Abandoned child/family. Broke sacred oath. PRESENT SECRETS: Spy for rival faction (may be reformed or active). Cursed/dying (hidden illness). Prophesied to betray MC or save world. Bonded to demon/spirit. Actually in love with MC (or rival). Seeks item MC possesses. Hunting specific enemy traveling with party. DARK SECRETS: Plans to steal MC's bloodline. Cult member awaiting activation order. Actually undead/possessed. Heir to villainous organization. Responsible for tragedy in MC's past. Will transform into monster eventually. Doomed by prophecy. POSITIVE SECRETS: Secretly guardian angel assigned to protect MC. Prophesied hero of their own arc. Possesses hidden Divine bloodline. Knows location of inheritance site. Related to one of MC's parents. Formerly trained by Sovereign. Has ability that could save everyone (but huge cost). TRAGIC SECRETS: Loved one held hostage (cooperates with enemy to protect them). Memory wiped (true identity unknown even to them). Body hijacked by parasite/curse periodically. Twin sibling is villain MC must face. Will die if helps MC complete quest (knows but does anyway). BENIGN SECRETS: Embarrassing hobby (writes poetry, collects plushies). Secret talent (amazing cook, beautiful singer). Noble goal (building orphanage, funding hospital). Romantic past with another companion. Fan of MC before meeting (has wanted to meet them). AI INSTRUCTION: Secrets should be revealed at dramatically appropriate moments - loyalty threshold, personal quest, or crisis situation. Some secrets create conflict, others deepen bond. Layer revelations - first secret revealed at 60 loyalty, deeper secret at 80, final truth at 95+.

## New Economic System - Tiers and Points
- Entry ID: 1021
- Keywords: new economic system, economic system, wealth system, economy, wealth tiers, currency

SINVEIL ECONOMY OVERVIEW: To manage the massive wealth gap between mortals and cultivators, the world uses a Tiered Wealth System. AI INSTRUCTION: Do not track individual coin counts (copper/silver/gold). Instead, track the character's 'Wealth Tier' (Lifestyle) and 'Wealth Points' (Liquid Assets).

THE GOLDEN RULE OF TRIVIALITY: If a Player's Wealth Tier is HIGHER than an item's Tier, the cost is TRIVIAL. Do not deduct currency. Assume the player has enough loose change. (Example: A Tier 3 Cultivator does not pay for a Tier 1 meal).

See Entries 708 (Tiers) and 709 (Wealth Points) for mechanics.

## Item Cost Tiers Reference
- Entry ID: 1022
- Keywords: food cost, lodging, services, item tiers

ITEM COST TIERS:
TIER 1 ITEMS: Street food, ale, inn rooms, basic steel weapons, torches, rations, clothing, common herbs, basic services.
TIER 2 ITEMS: Fine wine, luxury suites, Spirit Iron weapons, Uncommon pills, horses, minor information, quality equipment, healing services.
TIER 3 ITEMS: Rare techniques, Spirit Stones (low-grade), magical artifacts, mansions, formation arrays, sect secrets, Epic pills, legendary materials.
TIER 4 ITEMS: Legendary materials, Void-grade pills, skyships, territory rights, armies, ancient inheritances, Mythic techniques.

AI INSTRUCTION: When player asks 'how much?', determine item tier and compare to their Wealth Tier. If item tier is lower, say 'You can easily afford this' and don't charge. If equal or higher, reference Wealth Points cost (see Entry 709).

## REFERENCE ONLY - Cultivation Resources by Realm (Use Tiers)
- Entry ID: 1023
- Keywords: pills, elixirs, spirit herbs, cultivation resources, REFERENCE ONLY

REFERENCE ONLY - For flavor and NPC dialogue. Use Wealth Tiers for actual purchases.

BRONZE REALM RESOURCES (Tier 1): Qi Gathering Pill (Common), Healing Salve, Spirit Herb (Bronze-grade), Foundation Pill (Uncommon), Breakthrough Pill (Rare). IRON REALM RESOURCES (Tier 2): Iron Body Pill (Common), Qi Condensing Elixir (Uncommon), Spirit Herb (Iron-grade), Beast Core (Bronze/Iron), Breakthrough Pill (Epic). SILVER REALM RESOURCES (Tier 2-3): Silver Lotus Extract (Uncommon, Tier 2), Domain Seed Pill (Rare, Tier 3), Spirit Herb (Silver-grade), Low-Grade Spirit Stone (Tier 3), Breakthrough Pill (Legendary, Tier 3). GOLD REALM RESOURCES (Tier 3): Goldflame Essence (Rare), Immortal Foundation Pill (Epic), Spirit Herb (Gold-grade), Mid-Grade Spirit Stone, Bloodline Awakening Elixir (Mythic), Breakthrough Pill (Mythic). ASTRAL+ REALM RESOURCES (Tier 3-4): Most traded in sect contribution or favors rather than standard currency.

AI INSTRUCTION: When player wants to buy pills, determine tier from above and use Entry 709 (WP) purchasing rules.

## REFERENCE ONLY - Technique Manual Pricing (Use Tiers)
- Entry ID: 1024
- Keywords: technique prices, manual cost, technique scroll, REFERENCE ONLY

REFERENCE ONLY - For flavor and NPC dialogue. Use Wealth Tiers for actual purchases.

Technique Tier Guidelines: Common techniques = Tier 1. Uncommon techniques = Tier 1-2 depending on realm. Rare techniques = Tier 2-3. Epic techniques = Tier 3. Legendary techniques = Tier 3-4. Mythic techniques = Tier 4. Divine techniques = Priceless/quest rewards.

Realm affects tier: Bronze/Iron techniques are generally 1 tier lower than Silver/Gold equivalent techniques of same rarity.

AI INSTRUCTION: When player wants to buy techniques, determine tier based on rarity + realm, then use Entry 709 (WP) purchasing rules.

## REFERENCE ONLY - Equipment Pricing (Use Tiers)
- Entry ID: 1025
- Keywords: weapon prices, armor cost, equipment prices, REFERENCE ONLY

REFERENCE ONLY - For flavor and NPC dialogue. Use Wealth Tiers for actual purchases.

Equipment Tier Guidelines: Mortal equipment (no qi) = Tier 1. Common Spirit equipment = Tier 1-2. Uncommon Spirit equipment = Tier 2. Rare Spirit equipment = Tier 2-3. Epic Spirit equipment = Tier 3. Legendary Spirit equipment = Tier 3-4. Mythic Spirit equipment = Tier 4. Divine Spirit equipment = Tier 4-5/Priceless.

AI INSTRUCTION: When player wants to buy equipment, determine tier based on quality/rarity, then use Entry 709 (WP) purchasing rules.

## REFERENCE ONLY - Services Pricing (Use Tiers)
- Entry ID: 1026
- Keywords: services cost, healing prices, formation cost, REFERENCE ONLY

REFERENCE ONLY - For flavor and NPC dialogue. Use Wealth Tiers for actual purchases.

Service Tier Guidelines: Basic mortal services (healing, lodging, basic crafting) = Tier 1. Cultivator services (qi healing, formation installation, spiritual cuisine) = Tier 2. Advanced services (high-realm healing, complex formations, rare information) = Tier 3. Master services (Void+ healing, spatial formations, strategic intelligence) = Tier 4.

AI INSTRUCTION: When player wants services, determine tier based on complexity and provider's realm, then use Entry 709 (WP) purchasing rules.

## REFERENCE ONLY - Typical Wealth by Realm (Use Tiers)
- Entry ID: 1027
- Keywords: wealth by realm, cultivator income, REFERENCE ONLY

REFERENCE ONLY - For flavor and NPC characterization.

Typical Wealth Tiers by Realm: Bronze cultivators = Tier 1 (Survival). Iron cultivators = Tier 1-2 (Survival to Established). Silver cultivators = Tier 2 (Established). Gold cultivators = Tier 2-3 (Established to Ascendant). Astral cultivators = Tier 3 (Ascendant). Void cultivators = Tier 3-4 (Ascendant to Sovereign). Eternal cultivators = Tier 4 (Sovereign). Sovereign cultivators = Tier 5 (Cosmic).

Wealth within tier varies based on: Sect affiliation (steady income), success as mercenary/adventurer (variable), family wealth (inheritance), loot from dungeons/enemies.

AI INSTRUCTION: Use this for estimating NPC wealth levels and determining if they can afford to hire MC or offer rewards.

## Treasure and Reward Guidelines (UPDATED FOR WP)
- Entry ID: 1028
- Keywords: treasure generation, loot tables, reward scaling, wealth points, WP, loot, treasure

For AI narrator: Use these guidelines when generating loot and rewards. Award WEALTH POINTS (WP) for external content, SECT CONTRIBUTION POINTS (SCP) for sect content.

ENEMY LOOT BY DIFFICULTY:
MINOR ENEMY (trash mob, significantly weaker): No WP, just consumables/materials.
STANDARD ENEMY (equal realm/level): 10% chance of +1 WP.
ELITE ENEMY (mini-boss, higher realm): +1 WP guaranteed.
BOSS ENEMY (major fight, dungeon boss): +1 to +3 WP depending on difficulty.
LEGENDARY ENEMY (realm+ above, story boss): +3 to +5 WP.

EXTERNAL QUEST REWARDS (Side, Regional, Random):
MINOR QUEST (simple task, no combat): +1 WP.
MODERATE QUEST (standard difficulty): +1 to +2 WP.
MAJOR QUEST (multi-stage, dangerous): +2 to +3 WP.
EPIC QUEST (realm-threatening, major story): +3 to +5 WP.
LEGENDARY QUEST (world-changing): +5 to +10 WP.

SECT MISSION REWARDS (Primary = SCP, see Entry 582 (Quest System) & Entry 718 (SCP System)):
Sect missions award SCP as PRIMARY reward (10-500 based on type).
Dangerous sect missions (Defense, Assault, Crisis) may also include +1-2 WP as SECONDARY reward.
Sect Standing improves with all sect missions.

EXPLORATION REWARDS:
Hidden cache/chest: +1 WP.
Ancient ruin (cleared): +2 to +4 WP.
Inheritance site (completed): +3 to +10 WP + techniques/items.
Sovereign legacy: +10 WP + tier advancement possible.

ADDITIONAL LOOT:
Always include consumables (pills, talismans) appropriate to enemy realm.
Elite+ enemies drop equipment (weapons/armor) of their quality tier.
Bosses may drop technique scrolls or rare materials.
Legendary enemies drop unique items (named weapons, bloodline catalysts).
For legendary item rewards (inheritance sites, sovereign legacies, epic quest completions), see Entry 6318 for the 16 named artifacts.

AI NARRATOR GUIDELINES:
- Match rewards to challenge difficulty
- Don't flood with WP - scarcity creates tension
- Exceptional victories deserve exceptional rewards
- Failed quests can offer partial WP/SCP or alternative gains
- Sect missions = SCP primary, external = WP primary

SEE ALSO: Entry 582 (Quest System), Entry 718 (SCP System), Entry 720 (Quest Generation Template), Entry 721 (Item Generation Template).

REALM LOOT CEILINGS:
AI must enforce maximum obtainable tier based on MC's current realm.

BRONZE REALM (Tier 1 Lifestyle):
- Equipment: Tier 2 maximum (Superior Quality)
- Techniques: Uncommon maximum (Common preferred)
- Artifacts: None (Tier 3+ requires Silver minimum)
- Spatial Storage: Small pouch only (no spatial rings until Iron)
- Pills/Consumables: Common quality only

IRON REALM (Tier 2 Lifestyle):
- Equipment: Tier 3 maximum
- Techniques: Rare maximum
- Artifacts: Tier 3 (minor artifacts)
- Spatial Storage: Common spatial ring available

SILVER+ REALM:
- No artificial caps; use standard tier system from Entry 708/709

ENFORCEMENT:
If loot generation would exceed realm ceiling:
1. Downgrade to ceiling tier, OR
2. Mark as "damaged/sealed" - requires next realm to unlock, OR
3. Present as "too powerful to safely wield" - risk injury if equipped

EXCEPTION: Story-critical items may exceed ceiling but remain sealed/dormant until appropriate realm.

## Economic Tier System - Solves Currency Scaling
- Entry ID: 1029
- Keywords: economic tier system, economic tiers, tier system, purchasing power, trivial cost

ECONOMIC TIERS (LIFESTYLE):
TIER 0: DESTITUTE (Homeless)
- Currency Context: Begging for Copper.
- Trivial: None. Starving.
- Major Purchases: Food, shelter.

TIER 1: SURVIVAL (Mortal/Bronze)
- Currency Context: Counting Copper & Silver.
- Trivial: None. Every coin counts.
- Major Purchases: Basic gear, food, inn stays.

TIER 2: ESTABLISHED (Iron/Silver)
- Currency Context: Gold is standard.
- Trivial: Copper/Silver items (Meals, standard lodging, basic supplies are effectively free).
- Major Purchases: Rare materials, Spirit artifacts, sect fees.

TIER 3: ASCENDANT (Gold/Astral)
- Currency Context: Spirit Stones (Low/Mid).
- Trivial: Gold items (Mortal luxuries, mansions, common spirit weapons are effectively free).
- Major Purchases: Ancient relics, breakthrough pills, high-grade formations.

TIER 4: SOVEREIGN (Void/Eternal)
- Currency Context: High-Grade Stones, Favors, Territory.
- Trivial: Anything purchasable with mortal money or low-grade stones. True value is only found in unique treasures or barter.

TIER 5: COSMIC (Sovereign/Primordial)
- Currency Context: Reality-altering resources.
- Trivial: Everything below Divine tier.

WEALTH TIER ADVANCEMENT: Realm breakthrough typically increases Wealth Tier by 1 (Bronze->Iron = Tier 1->2). Major windfalls (inheritance, defeating wealthy enemy) can increase tier. Catastrophic losses can decrease tier.

## Wealth Points - Handling Major Purchases
- Entry ID: 1030
- Keywords: wealth points, wealth point, WP, purchasing rules, buying items, spend WP

WEALTH POINTS (WP):
While 'Wealth Tier' tracks lifestyle/triviality, 'Wealth Points' track liquid assets (Loot, Spirit Stones, Rewards).

PURCHASING RULES:
1. BELOW TIER: Free. (Tier 3 buys Tier 1 & 2 items for free).
2. AT TIER: Costs 1 WP. (Tier 3 buys Tier 3 item for 1 WP).
3. ABOVE TIER: Costs 3 WP per tier gap. (Tier 2 buys Tier 3 item for 3 WP. Tier 1 buys Tier 3 item for 6 WP).

GAINING WP:
- Completing a Quest: +1 WP.
- Looting a Boss/Dungeon: +1 to +3 WP depending on difficulty.
- Selling a Major Item: +1 WP (can only sell items at-tier or above).
- Windfall/Inheritance: +3 to +10 WP.

LOSING WP:
- Purchasing items (see rules above).
- Catastrophic loss (spatial ring destroyed, robbed): -50% of current WP.
- If WP drops below 0, reduce Wealth Tier by 1 and reset WP to 3.

STARTING WP: Based on difficulty mode. Normal = 3 WP, Easy = 5 WP, Hard = 2 WP, Very Hard = 1 WP.

MAXIMUM WP: Capped at 100 to prevent runaway wealth accumulation and maintain meaningful purchasing decisions.

## Sin Artifact Bonding System - Core Mechanics
- Entry ID: 1031
- Keywords: Sin Artifact, artifact bonding, artifact stage, Dormant artifact, Awakened artifact, Ascended artifact

SIN ARTIFACT BONDING SYSTEM: The Seven Sin Artifacts are semi-sentient divine-tier items that bond with wielders over time. Bonding progresses through three stages: Dormant, Awakened, Ascended. BONDING STAGES: DORMANT = Newly claimed or resisted. Artifact fights wielder's control. Limited power access. 1.5x domain size multiplier. +25% Sin technique power. Corruption aura: 5m radius. Wielder gains +5% corruption per week. AWAKENED = Bonded and cooperative. Artifact responds willingly. 2.0x domain size multiplier. +50% Sin technique power. +25% to primary stat. Corruption aura: 25m radius. Wielder gains +2% corruption per week. Can use artifact's signature ability at half power. ASCENDED = Fully mastered. Artifact and wielder are unified. 3.0x domain size multiplier. +100% Sin technique power. +50% to primary stat. +25% to all other stats. Corruption aura: 100m radius. Wielder corruption stabilizes (no further gain). Full access to artifact's signature ability. Can channel artifact power into any technique. BONDING TIME: Dormant->Awakened typically requires 50-200 years of use. Awakened->Ascended requires 500-2000 years. Current Generals have wielded artifacts for ~3,000 years since the Great Betrayal.

## Sin Artifact Domain System
- Entry ID: 1032
- Keywords: artifact domain, Sin domain boost, General domain power, Sin Artifact domain, artifact domain boost, General domain

SIN ARTIFACT DOMAIN SYSTEM: Sin Artifacts multiply the wielder's base Domain size.

DOMAIN SIZE FORMULA: Final Domain = (Bloodline Size) x (Artifact Multiplier) x (WIL / 50) x (Realm Factor). Note: Realm Factor is for Domain Clashes only (Void=1.0, Eternal=1.3), separate from Technique Damage multipliers.

ARTIFACT MULTIPLIERS: Dormant (newly claimed) = 1.5x. Awakened (bonded) = 2.0x. Ascended (fully mastered) = 3.0x.

EXAMPLE CALCULATIONS: Duke Calderon (Wrath, peak Void): Bloodline Ancient (1.0) x Ascended (3.0) x WIL 100 (2.0) x Void (1.0) = 6.0 domain strength. Lord Vaelen (Pride, mid Eternal): Bloodline Divine (5.0) x Ascended (3.0) x WIL 100 (2.0) x Eternal (1.3) = 39.0 domain strength. Primordial MC (Void, no artifact): Bloodline Primordial (10.0) x None (1.0) x WIL 90 (1.8) x Void (1.0) = 18.0 domain strength. DOMAIN CLASH RESULTS: Calderon vs MC: 6.0 vs 18.0 = MC wins (3:1 ratio, Major suppression). Vaelen vs MC: 39.0 vs 18.0 = Vaelen wins (2:1 ratio, Moderate suppression).

SIN DOMAIN EFFECTS: Within artifact-boosted domain, Sin corruption spreads. Orthodox cultivators must make WIL save each round or gain +1% corruption. Light Path techniques suffer -30% effectiveness. Sin techniques gain bonus equal to artifact stage (+25% Dormant/+50% Awakened/+100% Ascended).

CURRENT GENERAL ARTIFACT STATUS: Vaelen (Pride) = Ascended, Crown of Pride fully mastered. Aurex (Greed) = Ascended, Vault of Greed fully mastered. Vespera (Temptation) = Awakened, Chains of Temptation bonded but not perfected. Elowen (Envy) = Awakened, Mirror of Envy reflects but not perfectly. Glut (Gluttony) = Ascended, Maw of Gluttony fully mastered. Calderon (Wrath) = Ascended, Hammer of Wrath fully mastered. Morvane (Sloth) = Dormant, Veil of Sloth resists even its wielder.

SIN BLOOD ASCENSION (Balance Rule): Generals bonded to Sin Artifacts (Awakened+) are transformed by the sin. For Domain calculations, their Bloodline Size is treated as DIVINE (Multiplier 5.0), regardless of their original race. This ensures Generals remain threats even to Primordial bloodlines.

## Current General Artifact Status
- Entry ID: 1033
- Keywords: current artifact status, General artifact level, Vaelen artifact, Calderon artifact

CURRENT GENERAL ARTIFACT STATUS: Each General claimed their Sin Artifact during the Great Betrayal ~3,000 years ago. Mastery varies based on compatibility and effort. LORD VAELEN (Pride) - Crown of Pride: ASCENDED. Perfect compatibility. Crown amplifies his natural arrogance. 3,000 years of absolute mastery. Domain strength with artifact: 39.0 (mid Eternal + Divine bloodline). LADY AUREX (Greed) - Vault of Greed: ASCENDED. Hoarded power obsessively. Vault contains millennia of stolen techniques. Domain strength: 26.0 (mid Eternal + Divine bloodline). COUNTESS VESPERA (Temptation) - Chains of Temptation: AWAKENED. Chains require genuine desire to fully bond. Vespera's calculated nature limits connection. Domain strength: 17.3 (low Eternal + Divine bloodline). SISTER ELOWEN (Envy) - Mirror of Envy: AWAKENED. Mirror reflects wielder's insecurity. Elowen's jealousy feeds it but also destabilizes bond. Domain strength: 8.0 (peak Void + Ancient bloodline). BARON GLUT (Gluttony) - Maw of Gluttony: ASCENDED. Perfect symbiosis. Glut IS hunger. Maw grows with every meal. Domain strength: 6.0 (mid Void + Ancient bloodline). DUKE CALDERON (Wrath) - Hammer of Wrath: ASCENDED. Rage forged absolute bond. Hammer responds to fury instantly. Domain strength: 6.0 (peak Void + Ancient bloodline). LORD MORVANE (Sloth) - Veil of Sloth: DORMANT. Paradox: mastering Sloth requires effort. Morvane too apathetic to bond. Veil barely responds. Domain strength: 1.5 (low Void + Ancient bloodline).

## Sin Artifact Signature Abilities
- Entry ID: 1034
- Keywords: artifact signature ability, Crown ability, Hammer ability, Vault ability

SIN ARTIFACT SIGNATURE ABILITIES: Each artifact grants a unique power beyond domain boosting. Power scales with bonding stage. CROWN OF PRIDE - Absolute Command: Force obedience from beings of lower realm who meet wielder's gaze. Dormant: 1 realm below, 10 seconds. Awakened: 2 realms below, 1 minute. Ascended: 3+ realms below, until dismissed or realm gap closed. Primordial bloodlines resist at -50% duration. VAULT OF GREED - Infinite Hoarding: Store and instantly summon any object, technique, or soul. Dormant: 100 item limit, 1 second summon delay. Awakened: 10,000 items, instant summon, can store techniques. Ascended: Unlimited storage, can summon stored souls as temporary servants. CHAINS OF TEMPTATION - Binding Desire: Chains manifest from target's deepest wants. Dormant: Physical binding only, STR check to escape. Awakened: Binds will, target must pursue offered desire. Ascended: Can permanently bind souls through fulfilled promises. MIRROR OF ENVY - Perfect Reflection: Copy techniques and bloodline abilities. Dormant: Copy 1 technique, lasts 1 hour, 50% power. Awakened: Copy 3 techniques, lasts 1 day, 75% power. Ascended: Copy unlimited techniques, permanent until replaced, 100% power. Can copy bloodline passives. MAW OF GLUTTONY - Absolute Consumption: Devour matter, qi, techniques, concepts. Dormant: Physical matter only, building-sized maximum. Awakened: Can devour qi attacks and techniques mid-cast. Ascended: Can devour abstract concepts (devour someone's 'speed' or 'sight' temporarily). HAMMER OF WRATH - Rage Amplification: Power scales with anger. Dormant: +50% damage when below 50% HP. Awakened: +100% damage scaling with rage, attacks cause fear. Ascended: +200% damage at peak rage, strikes can shatter space, immune to pain. VEIL OF SLOTH - Motivation Drain: Suppress willpower and cultivation. Dormant: -25% enemy cultivation speed in 100m. Awakened: -50% cultivation, -25% combat effectiveness. Ascended: Complete cultivation halt, enemies lose will to fight (WIL save or surrender).

## Claiming Sin Artifacts - Mortal Path
- Entry ID: 1035
- Keywords: claim Sin Artifact, mortal artifact wielder, MC artifact

CLAIMING SIN ARTIFACTS: Sin Artifacts can theoretically be claimed by anyone who defeats the current wielder. For mortals, this creates unique challenges and opportunities. CLAIMING REQUIREMENTS: Must personally strike killing blow on current wielder. Must touch artifact within 1 hour of wielder's death. Must survive initial bonding (WIL check DC 25 + wielder's realm level). MORTAL WIELDER EFFECTS: Artifact immediately attempts corruption. Gain +15% corruption upon claiming. Dormant stage bonuses apply immediately. Begin Dormant->Awakened progression. CORRUPTION RESISTANCE: Primordial bloodlines gain +50% resistance to artifact corruption. Light Path cultivators can purify artifact corruption (slow, painful process). Orthodox artifact use is possible but requires constant purification to avoid falling. SIN SOVEREIGN PROPHECY: Ancient texts suggest wielding multiple Sin Artifacts creates compounding power. Two artifacts = 1.5x combined effect. Three artifacts = 2x combined effect. All seven = 'Sin Sovereign' status, power beyond normal Sovereign realm. The prophecy is ambiguous about whether Sin Sovereign would be devil or purified mortal. MC PATH OPTIONS: 1) Destroy artifacts (removes General's power source, difficult). 2) Claim and purify (become anti-corruption wielder, requires Light Path mastery). 3) Claim and embrace (corruption path, massive power, eventual fall). 4) Seal artifacts (temporary solution, others can unseal). NARRATIVE NOTE: Artifact claiming is late-game content. Void+ realm recommended minimum. Eternal realm for realistic success chance against Generals.

## Artifact Bonding Progression
- Entry ID: 1036
- Keywords: artifact bonding progression, accelerate bonding, artifact mastery

ARTIFACT BONDING PROGRESSION: Bonding advances through use, alignment, and time. STANDARD PROGRESSION: Dormant->Awakened: 50-200 years. Awakened->Ascended: 500-2000 years. Total to Ascended: 550-2200 years. Current Generals had 3,000 years. ACCELERATING FACTORS: Sin Alignment: Acting in accordance with artifact's Sin accelerates bonding. Pride artifact bonds faster when wielder demonstrates superiority. Wrath bonds through destruction. Sloth through... doing nothing (paradox). Major Sin Acts: Performing significant acts of the Sin grants +5-20 years equivalent progress. Calderon's continent-shaking rages. Glut's consumption of entire cities. Artifact Resonance: Using artifact's signature ability frequently. Killing with artifact (souls partially absorbed). Defeating rivals who threaten wielder's Sin domain. SLOWING FACTORS: Resistance: Fighting the Sin slows bonding. Orthodox wielders progress 5x slower. Purification: Light Path purification can reverse bonding progress. Disuse: Artifacts not used regularly may regress (rare, requires centuries of neglect). Internal Conflict: Elowen's jealousy of other Generals ironically slows her bond (envy of their progress). MORVANE PARADOX: Veil of Sloth requires effort to master. Morvane is too slothful to put in effort. After 3,000 years, still Dormant. This makes him simultaneously the weakest General in direct combat and potentially the most dangerous (if he ever tried). AI NOTE: Artifact progression is background lore. MC would start Dormant if claiming artifact. Reaching Awakened within campaign timeframe possible with heavy Sin usage. Ascended is endgame/epilogue territory.

## Fighting Sin Artifact Wielders
- Entry ID: 1037
- Keywords: artifact combat, fighting artifact wielder, counter Sin Artifact

FIGHTING SIN ARTIFACT WIELDERS: Strategies for combating Generals and their artifacts. GENERAL PRINCIPLES: Artifact power scales with bonding stage - target weaker-bonded Generals first. Domain clash is critical - losing domain means fighting suppressed. Sin Artifacts amplify weaknesses as well as strengths. COUNTER-STRATEGIES BY ARTIFACT: CROWN OF PRIDE: Never meet Vaelen's gaze directly. Fight from range or with eyes closed. Pride blinds - exploit overconfidence. Humiliation enrages and destabilizes. VAULT OF GREED: Aurex relies on hoarded techniques - unpredictable attack patterns. Target the Vault directly if possible. She hoards everything including weaknesses. CHAINS OF TEMPTATION: Resist desire, maintain emotional control. Chains can't bind those who want nothing. Monks and ascetics have advantage. MIRROR OF ENVY: Elowen copies your best techniques - use techniques with hidden costs. Bait with flashy moves, punish with fundamentals. Her copied abilities lack true mastery. MAW OF GLUTTONY: Don't let attacks get devoured - Glut grows stronger. Fast, precise strikes before Maw can react. Starving Glut weakens him significantly. HAMMER OF WRATH: Keep Calderon calm - rage amplifies power. Hit-and-run tactics frustrate but don't enrage. Killing allies in front of him is suicide (rage spike). VEIL OF SLOTH: Hardest to fight - Veil drains will to continue. Light Path techniques resist apathy. Must defeat quickly before motivation drains. Morvane rarely fights directly anyway. PARTY TACTICS: Designate one member to distract artifact ability. Tank absorbs signature power while others damage. Light Path support counters corruption aura. Multiple attackers prevent artifact focus.

## Artifact Destruction and Sealing
- Entry ID: 1038
- Keywords: artifact destruction, destroy Sin Artifact, seal artifact

ARTIFACT DESTRUCTION AND SEALING: Options for permanently removing Sin Artifacts from play. DESTRUCTION: Sin Artifacts are nearly indestructible. REQUIREMENTS: Sovereign-tier power or equivalent. Primordial bloodline technique specifically designed for purification. Sacrifice of equivalent power (life force, cultivation base, other artifact). Location with extremely pure qi (Sovereign tomb, creation site). EFFECTS OF DESTRUCTION: Corresponding Sin weakens across all Sinveil (-50% corruption spread). General loses all artifact bonuses immediately. Massive qi backlash may kill nearby cultivators. Sin energy disperses - may reform artifact in centuries. SEALING: Temporary but more achievable. REQUIREMENTS: Eternal realm minimum for sealing ritual. Formation knowledge at Master level. Rare sealing materials (Void-tier minimum). Location away from Sin influence. SEAL DURATION: Low-quality seal: 10-50 years. Standard seal: 100-500 years. Master seal: 1000-5000 years. Sovereign seal: 10,000+ years (what trapped Original Generals). SEALED ARTIFACT EFFECTS: Artifact power suppressed to Dormant equivalent. Wielder cannot access signature ability. Domain boost reduced to 1.0x (no bonus). Seal can be broken by: wielder reaching higher realm, external intervention, seal degradation over time. MC OPTIONS: Early game - flee from artifacts. Mid game - seal artifacts with help. Late game - destroy or claim artifacts. Endgame - collect multiple artifacts (Sin Sovereign path) or purify/destroy all (Orthodox Savior path).

## Sect Contribution Points System
- Entry ID: 1039
- Keywords: sect contribution points, sect contribution, contribution points, SCP, spend SCP, sect treasury, sect armory

SECT CONTRIBUTION POINTS (SCP): Internal currency used exclusively within your sect. Cannot be traded between sects or converted to Wealth Points. Represents your value and service to the sect.

EARNING SCP:
? Complete sect missions: 10-500 SCP based on difficulty
? Donate materials: 1 SCP per 0.1 WP value of materials
? Donate crafted items: Tier 2 Standard = 50 SCP, Tier 3 Superior = 300 SCP, Tier 4 Perfect = 2000 SCP
? Teach junior disciples: 5-20 SCP per session
? Defend sect territory: 50-200 SCP per battle
? Bring honor to sect (tournament victories, alliances): 100-1000 SCP
? Report valuable intelligence: 25-250 SCP

SPENDING SCP:
? Access sect technique library: Common = 50 SCP, Uncommon = 200 SCP, Rare = 1000 SCP, Epic = 5000 SCP
? Cultivation resources: Pills, herbs, beast cores at 50% market WP value in SCP (1 WP = 100 SCP)
? Personal training hall reservation: 10 SCP/day (basic), 50 SCP/day (advanced with formations)
? Elder instruction: 100-500 SCP per session
? Crafting workshop access: 25 SCP/day
? Request sect protection: 200-2000 SCP based on threat
? Borrow sect artifacts: 500-5000 SCP deposit (returned if artifact returned undamaged)

SCP AND SECT STANDING:
? High SCP earnings improve Sect Standing over time (+1 Standing per 500 SCP earned monthly)
? Low/negative SCP balance damages reputation (-1 Standing per month at 0 SCP)
? Core Disciples receive 50 SCP monthly stipend
? Inner Disciples receive 20 SCP monthly stipend
? Outer Disciples receive no stipend

SCP DEBT: Going negative is possible but dangerous. -100 SCP = demotion warning. -500 SCP = forced labor missions. -1000 SCP = expulsion proceedings. Debt can be cleared through dangerous missions or patron elder intervention.

NOTE: SCP exists separately from Wealth Points. A rich cultivator (high WP) may still be sect-poor (low SCP) if they don't contribute. Sect resources are NOT purchasable with external wealth - only service earns access.

SEE ALSO: Entry 700 (Wealth System), Entry 709 (Wealth Points), Entry 722 (Equipment Acquisition).

## Quest Generation Template
- Entry ID: 1040
- Keywords: quest generator, mission board, generate quest, quest template

QUEST GENERATOR: Use this format when generating quests or missions.

### ? QUEST: [Title]
*   **Type:** [Main Story / Sect Mission / Companion Personal / Side Quest / Regional / Daily / Bounty / Secret]
*   **Sect Mission Tier:** (If Sect Mission) [Errand / Patrol / Hunt / Investigation / Defense / Assault / Crisis]
*   **Objective:** [Clear verb + Target] (e.g., Hunt the Jade Tiger. Use Entry 719 for Sect Mission ideas)
*   **Location:** [Specific Region / Landmark] (Must exist in current zone or adjacent)
*   **Difficulty:** [Trivial (50 below) / Easy (20-49 below) / Normal (within 20) / Hard (20-49 above) / Deadly (50+ above) / Suicidal (1+ realm above)]
*   **Recommended Realm:** [Bronze / Iron / Silver / Gold / Astral / Void / Eternal]
*   **Party Size:** [Solo / 2-3 / Full Party (4)] (Recommended party composition)
*   **Time Limit:** [None / Urgent (1 day) / Standard (3 days) / Extended (1 week)]
*   **Rewards:**
    - **WP:** [0-5] (0 for trivial tasks, +1-2 for dangerous missions)
    - **SCP:** [10-500] (Sect missions only: Errand 10-25, Patrol 25-50, Hunt 50-100, Investigation 75-150, Defense 100-200, Assault 150-300, Crisis 200-500)
    - **Items:** [Specific loot or 'Tier X equipment'. Reference Entry 726 for recipes]
    - **Standing:** [+Minor / +Moderate / +Major] [Faction name]
    - **Special:** (Optional) [Technique scroll, Bloodline catalyst, Companion recruitment opportunity]
*   **Completion Bonuses:** Ahead of schedule: +50% SCP | Higher difficulty than required: +100% SCP, +1 WP | Perfect completion (no injuries): +25% all rewards
*   **Failure Consequences:** [None / Standing loss / SCP debt / Reputation damage / Story consequences]
*   **Twist:** [Hidden complication revealed mid-quest] (Betrayal, ambush, moral dilemma, false information, escalation)
*   **Chain Potential:** [None / Leads to: Quest Name] (Can this spawn follow-up quests?)

GUIDELINES: Main Story quests cannot be abandoned and offer major story progression with high rewards. Sect Missions use SCP as primary reward with WP only for dangerous tiers. Companion Personal quests unlock at 60+ loyalty and reward loyalty plus unique items/techniques. Secret Quests have hidden triggers with exceptional rewards and no quest log entry until discovered. Always match rewards to difficulty - deadly quests should feel worth the risk. Twists should be logical and foreshadowed when possible. SEE ALSO: Entry 582 (Quest System), Entry 693 (Treasure Generation), Entry 709 (Wealth Points), Entry 719 (Sect Missions), Entry 726 (Recipe Compendium).

## Item/Loot Generation Template
- Entry ID: 1041
- Keywords: item generator, loot generator, equipment template, artifact details

ITEM GENERATOR: Use this format when generating specific loot, equipment, or artifacts.

### ?? ITEM: [Name]
*   **Slot:** [Weapon / Head / Chest / Hands / Legs / Feet / Accessory / Consumable / Material]
*   **Weapon Class:** (If weapon) [Light (1d6) / Medium (1d8) / Heavy (1d12) / Ranged (1d8) / Unarmed]
*   **Armor Class:** (If armor) [Light (+2 Defense) / Medium (+4 Defense, -10% move) / Heavy (+6 Defense, -20% move) / Robes (+WIS Defense)]
*   **Quality:** [Inferior (-1 hit, -1 dmg) / Standard / Superior (+1 hit) / Perfect (+1 hit, +2 dmg)]
*   **Tier:** [1-Bronze / 2-Iron / 3-Silver / 4-Gold / 5-Astral / 6-Void / 7-Eternal / 8-Sovereign]
*   **Realm Requirement:** [None / Bronze / Iron / Silver / Gold / Astral / Void / Eternal] (Cannot equip below this realm)
*   **Stat Requirement:** (Optional) [STR 15 / DEX 12 / etc.] (Minimum stat to use effectively)
*   **Element Affinity:** [None / Sword / Spear / Staff / Body / Fire / Water / Earth / Wind / Lightning / Shadow / Light / Soul / Blood / Poison / Beast / Formation] (+10% technique damage when matching user's path)
*   **Effect:** [Passive Stat Bonus (+1-3 per tier) OR Active Ability (1/combat or 1/day)]
*   **Flaw:** (Corrupted/Cursed items only) [Drawback - stat penalty, corruption gain, or restriction]
*   **Corruption:** [None / Minor (+1%/week) / Moderate (+3%/week) / Major (+5%/week)]
*   **WP Value:** [Tier number] (Cost to purchase at-tier = 1 WP)
*   **Description:** [1-2 sentence visual description]

GUIDELINES: Tier 1-2 items grant +1-2 stats OR simple passive (e.g., +5 HP). Tier 3-4 items grant +2-4 stats OR moderate ability (e.g., 1/combat fire burst). Tier 5-6 items grant +4-6 stats OR strong ability with cooldown. Tier 7-8 items grant +6-10 stats OR reality-affecting abilities, semi-sentient possible. Path Affinity items should match weapon type (Sword Path = swords, Body Path = unarmed/gauntlets). Corrupted items offer +50% power but impose Flaw. Named/Legendary items should have unique lore-relevant names. SEE ALSO: Entry 597 (Base Combat - Weapon Damage), Entry 6301 (Combat Healing Usage Limits), Entry 6302 (Injury Recovery Items), Entry 6303 (Purification Items), Entry 696 (Equipment Tiers), Entry 693 (Treasure Generation), Entry 709 (Wealth Points).

## Equipment Acquisition Methods
- Entry ID: 1042
- Keywords: equipment acquisition, buy equipment, get spatial ring, purchase gear, equipment sources

EQUIPMENT ACQUISITION: How to obtain weapons, armor, accessories, and spatial storage.

METHOD 1 - WEALTH POINT PURCHASES (External):
Spend WP at merchants, traveling traders, auction houses, or city markets. Use Entry 709 purchasing rules: Below tier = free, At tier = 1 WP, Above tier = 3 WP per tier gap. Requires finding a seller with desired item. Common/Uncommon items readily available in cities. Rare+ items require special merchants, auctions, or connections.

METHOD 2 - SECT CONTRIBUTION POINTS (Internal):
Spend SCP at sect treasury/armory. Equipment costs: Tier 1 = 50 SCP, Tier 2 = 150 SCP, Tier 3 = 500 SCP, Tier 4 = 2000 SCP, Tier 5+ = Not available (quest/achievement only). SPATIAL RINGS via SCP: Common = 200 SCP (Silver+ to use), Uncommon = 500 SCP, Rare = 1500 SCP, Epic = 5000 SCP (Inner Disciple+ standing required). Legendary spatial rings cannot be purchased - only earned.

METHOD 3 - QUEST REWARDS:
Quest completion may grant equipment directly. See Entry 720 (Quest Template) for reward types. Major/Epic/Legendary quests commonly reward Tier 3+ equipment. Companion personal quests often grant unique items.

METHOD 4 - ENEMY LOOT:
Defeated enemies may drop equipment. See Entry 693 (Treasure Generation). Elite+ enemies drop equipment matching their realm tier. Bosses may drop named/unique items. Legendary enemies drop artifacts and bloodline catalysts.

METHOD 5 - CRAFTING:
Create equipment via Blacksmithing (weapons/armor) or Inscription (accessories/spatial items). See Entry 587 (Crafting). Requires recipe, materials, workspace, and skill check. Quality depends on roll: Inferior/Standard/Superior/Perfect.

METHOD 6 - INHERITANCE/DISCOVERY:
Exploring ancient ruins, inheritance sites, or hidden caches may yield equipment. Higher risk = higher tier rewards. Spatial rings occasionally found in treasure rooms.

SPATIAL RING SUMMARY:
? Common (50 slots): 1-2 WP or 200 SCP. Available at Silver realm.
? Uncommon (100 slots): 2-3 WP or 500 SCP. Available at Silver realm.
? Rare (200 slots): 3-4 WP or 1500 SCP. Available at Gold realm.
? Epic (500 slots): 5+ WP or 5000 SCP. Requires Inner Disciple standing. Available at Astral realm.
? Legendary (Unlimited): Quest/inheritance only. Cannot be purchased. Typically Void+ realm.

ATTUNEMENT: Spatial rings require Silver+ realm to attune. Lower realm cultivators cannot use them even if acquired.

SEE ALSO: Entry 588 (Inventory System), Entry 587 (Crafting), Entry 693 (Treasure Generation), Entry 709 (Wealth Points), Entry 718 (SCP System), Entry 721 (Item Generation Template).

## Legendary Item Attunement System
- Entry ID: 1043
- Keywords: legendary attunement, artifact bonding, legendary item limit, attunement system, legendary item slots

LEGENDARY ITEM ATTUNEMENT SYSTEM: Legendary (Tier 5+) and Mythic/Divine (Tier 6-8) items require attunement before their powers activate. This represents bonding with artifact on spiritual level.

ATTUNEMENT PROCESS:
1) Acquire legendary item through quest, inheritance, or discovery
2) Spend 24 hours in uninterrupted meditation with item (specific meditation requirements vary by item - some require combat, darkness, water immersion, etc.)
3) Item bonds to your qi signature and activates all powers
4) Once attuned, item recognizes you as wielder

ATTUNEMENT LIMITS:
Maximum 3 attuned legendary items simultaneously. This represents limit of mortal soul's capacity to channel multiple legendary powers.

CONSEQUENCES OF EXCEEDING LIMIT:
? 4 attuned items: Qi conflict, -3 to all stats (soul overwhelmed by competing powers)
? 5+ attempted attunements: Cannot attune (qi rejection, items refuse to bond)

BREAKING ATTUNEMENT:
? Standard: Meditate 1 hour to voluntarily break bond
? Cursed Items: May require longer (1 week for Muramasa) or special ritual
? Death: Breaks all attunements (items can be claimed by others)
? Theft: If item stolen while attuned, thief cannot use powers until they break your attunement and create their own (takes time, gives you chance to reclaim)

NON-LEGENDARY ITEMS: Tier 1-4 items do NOT require attunement. Can be equipped/used immediately.

SEE ALSO: Entry 721 (Item Generation Template), Entry 696 (Equipment Tiers), Entry 6318 (Legendary Artifact Index).

## Equipment Notoriety System
- Entry ID: 1044
- Keywords: equipment notoriety, weapon notoriety, artifact notoriety, famous weapon, legendary weapon, recognizable items

EQUIPMENT NOTORIETY: Wielding recognizable legendary artifacts increases notoriety. Famous weapons and armor make you visible to factions across regions.

NOTORIETY IMPACT BY ITEM TYPE:
- WELL-KNOWN ARTIFACTS: +20-30 notoriety while equipped (Muramasa, Tidekeeper's Trident, etc.)
- ALWAYS-VISIBLE ITEMS: +25-50 notoriety FLOOR while equipped (Celestial Halo, Worldbreaker, Dawnbringer)
- CURSED/INFAMOUS ITEMS: +30 notoriety + increased General attention (Muramasa, Shadowfang)
- DIVINE/HOLY ITEMS: +20-50 notoriety + demon faction targeting (Heaven's Decree, Celestial Halo)

SCHEMA TRACKING: Use equipmentNotorietyFloor field (format: 'VALUE|EXPIRY').

EQUIP RULES:
1. On equip legendary with floor bonus: Set equipmentNotorietyFloor = 'VALUE|EQUIPPED'
2. Effective floor = max(notorietyFloor, equipmentFloor value if not expired)
3. Example: Equip Celestial Halo (+50) -> set '50|EQUIPPED'

UNEQUIP RULES:
1. On unequip: Change EXPIRY from 'EQUIPPED' to 'Month X' where X = currentMonth + (1-3)
2. Linger duration: 1 month (minor items), 2 months (major), 3 months (legendary/divine)
3. Example: Unequip in Month 5 -> change '50|EQUIPPED' to '50|Month 7'
4. Floor remains active until expiry (reputation lingers as stories spread)

MONTHLY DECAY CHECK:
1. If currentMonth >= expiry month: Clear equipmentNotorietyFloor to empty string
2. Effective floor reverts to sect rank floor (notorietyFloor field)

STATE EXAMPLES:
Equip: sectFloor=25, equipFloor='50|EQUIPPED', effective=50
Unequip (Month 5): sectFloor=25, equipFloor='50|Month 7', effective=50
Month 8: sectFloor=25, equipFloor='' (cleared), effective=25

MULTIPLE ITEMS: Only track highest floor. If equipping new legendary, overwrite equipmentNotorietyFloor.

AI INSTRUCTION: When player equips/unequips legendary, update equipmentNotorietyFloor. On month advance, check expiry. Inform player of notoriety impact.

SEE ALSO: Entry 592 (Notoriety System), Entry 593 (Sect Standing), Entry 6318 (Legendary Artifact Index).

## Stat Cap Exceptions for Legendary Items
- Entry ID: 1045
- Keywords: legendary stat bonuses, stat cap increase, exceeding stat cap, legendary item stats, stat limit exceptions

LEGENDARY ITEM STAT BONUSES: Legendary and higher-tier items can grant two types of stat modifications.

TYPE 1 - STAT CAP INCREASES:
Legendary items can increase stat CAPS by up to +20 (allowing allocation beyond realm cap).
- Gold realm (cap 85) + Worldbreaker (+10 cap) = can allocate up to 95
- Schema support: core stats can store up to 120 to preserve allocated points under cap-increase gear
- On UNEQUIP: Points above realm cap become INACTIVE (stored but capped at realm limit for rolls AND derived stats like PER/INIT)
- NO TRACKING NEEDED - AI just enforces realm cap when the cap-increase item is not equipped

CAP INCREASE STACKING:
Multiple cap increase sources do NOT stack - HIGHEST single source applies per stat.
Formula: Effective Cap = Base Realm Cap + max(all cap bonuses for that stat)

Example (Gold realm, cap 85):
- Atlas Mantle (+20 STR cap) + Worldbreaker (+10 STR cap)
- STR effective cap = 85 + max(20, 10) = 105 (NOT 115)

Example (2 items + 1 technique):
- Worldbreaker: +10 STR cap
- Crown of Dominion: +15 WIL cap
- Titan's Endurance technique: +5 CON cap
Result: STR cap=95, WIL cap=100, CON cap=90, others=85

TYPE 2 - TEMPORARY STAT BONUSES:
Some items grant '+X to STAT' that apply immediately. THESE MUST BE TRACKED.

SCHEMA TRACKING (equipmentStatBonuses field):
Format: 'STAT:+VALUE,STAT:+VALUE' or empty string.
Example: 'STR:+10,CON:+5' means +10 STR and +5 CON from equipment.
Effective stat = base stat + equipment bonus.

EQUIP RULES:
1. If item grants stat BONUS (not cap increase): Include it in equipmentStatBonuses
2. Example: Equip Atlas Mantle (+10 CON bonus) -> bonuses='CON:+10'
3. Multiple items: bonuses='STR:+10,CON:+5,WIS:+3'

UNEQUIP RULES:
1. On any equip/unequip, REWRITE equipmentStatBonuses from scratch based on currently equipped items (do not incrementally add/subtract)
2. Effective stats recalculate automatically
3. Base stats (allocated points) remain unchanged

CAP INCREASE ON UNEQUIP:
1. Check if any base stat exceeds realm cap
2. If yes: stat is CAPPED at realm limit for all rolls (and derived stats)
3. Allocated points are NOT lost - just dormant until cap raised again

STATE EXAMPLE:
Equip: STR=70, bonuses='STR:+10', effective=80
Level up (allocate 5 to STR): STR=75, bonuses='STR:+10', effective=85
Unequip: STR=75, bonuses='', effective=75

MAXIMUM STAT: 120 (base 100 cap + 20 from legendary equipment).

SEE ALSO: Entry 600 (Core Stats), Entry 599 (Stat Caps by Realm), Entry 6318 (Legendary Artifact Index).

## Equipment Slot Clarifications
- Entry ID: 1046
- Keywords: equipment slots, armor slots, weapon slots, shield slot, gauntlet slot, cloak slot, two-handed weapons

EQUIPMENT SLOT CLARIFICATIONS: Standard equipment slots with special cases for unique items.

STANDARD SLOTS (Unchanged):
? WEAPON: 1-2 slots (single weapon OR dual-wield OR one two-handed weapon using both slots)
? ARMOR: 1 slot (full set OR single piece that provides torso/body coverage)
? ACCESSORIES: 3 slots maximum (traditionally 2 rings + 1 amulet, but flexible)

SPECIAL EQUIPMENT TYPES:

SHIELDS:
Shields can occupy either:
? OPTION A: Off-hand weapon slot (traditional - shield in one hand, weapon in other)
? OPTION B: Armor slot (tower shields that provide full body protection in place of armor)
? Player chooses during equip/attunement which slot to use
? Example: Titan's Aegis can be equipped in weapon slot (keep armor) OR armor slot (full protection)

TWO-HANDED WEAPONS:
? Occupy BOTH weapon slots (cannot use anything else in hands)
? Examples: Greatswords, war hammers, polearms, greataxes
? Worldbreaker Greatsword, Dawnbringer Hammer both require two hands

CLOAKS/ROBES/MANTLES:
? Occupy armor slot (provide torso/body coverage)
? Examples: Stormcaller's Mantle, Voidweaver Robes, Atlas Mantle
? Cannot wear traditional armor AND legendary cloak (overlapping coverage)

GAUNTLETS/GLOVES:
? Single gauntlet: 1 accessory slot
? Pair of gauntlets: 2 accessory slots (both hands)
? Examples: Earthshaker Gauntlets (pair, 2 slots), Fist of the Immortal (right hand only, 1 slot)

PAULDRONS/SHOULDERS:
? Occupy armor slot (shoulder coverage considered armor piece)
? Example: Atlas Mantle (shoulders + back = armor slot)

HEADPIECES:
? Light headpieces (circlets, halos): Accessory slot
? Heavy headpieces (helmets): Armor slot (if using piece-by-piece armor system)
? Example: Phoenix Crown (circlet = accessory), Celestial Halo (floating = accessory)

PIECE-BY-PIECE ARMOR (Optional Rule):
Current system uses single "armor" slot for simplicity. DMs may choose to allow:
? Head, Chest, Legs as separate slots
? This is optional complexity - default is single armor slot
? If using piece-by-piece: Total 3 armor slots instead of 1

AI INSTRUCTION: When player acquires equipment, clearly state which slot it occupies. For ambiguous items (shields, cloaks), offer player choice during equip.

SEE ALSO: Entry 588 (Inventory System), Entry 721 (Item Generation), Entry 6318 (Legendary Artifact Index).

## Weapon Damage Baseline & Legendary Scaling
- Entry ID: 1047
- Keywords: weapon damage, damage formula, legendary weapon damage, weapon scaling, damage calculation

WEAPON DAMAGE SCALING: Base weapon damage dice plus stat-based scaling.

BASE WEAPON DAMAGE BY CLASS (Unchanged):
? Light Weapons (daggers, short swords): 1d6
? Medium Weapons (longswords, spears, maces): 1d8
? Heavy Weapons (greatswords, war hammers, greataxes): 1d12
? Ranged Weapons (bows, crossbows): 1d8
? Unarmed/Improvised: 1d4

STAT MODIFIERS:
? Add relevant stat modifier to damage: [STAT / 5] rounded down
? Example: STR 45 = +9 damage modifier
? Melee weapons use STR, ranged use DEX, some special weapons use WIS

LEGENDARY WEAPON DAMAGE:
Legendary weapons add SCALING BONUSES on top of base damage:
? Base dice (1d6, 1d8, or 1d12)
? + Stat modifier ([STAT / 5])
? + Legendary scaling bonus (additional [STAT x 1-3] depending on weapon)

EXAMPLE CALCULATIONS:

Worldbreaker Greatsword (Heavy, Legendary):
? Base: 1d12 (heavy weapon)
? + [STR / 5] (normal stat mod)
? + [STR x 2] (legendary scaling)
? + Armor Sundering (ignore 50% enemy AC)
? = Very high damage for titan weapon

Shadowfang Dagger (Light, Legendary):
? Base: 1d6 (light weapon)
? + [DEX / 5] (normal stat mod)
? + [DEX x 3] (legendary scaling - speed weapon)
? + Ignore AC (phase through defenses)
? = Lower base but bypasses armor

MAGICAL WEAPON PROPERTY:
All Legendary weapons automatically count as magical for purposes of:
? Bypassing "resistance to non-magical damage"
? Hitting incorporeal/ethereal creatures
? Affecting demons/spirits that require magical weapons

QUALITY MODIFIERS STILL APPLY:
? Inferior: -1 to hit, -1 damage
? Standard: No modifier
? Superior: +1 to hit
? Perfect: +1 to hit, +2 damage
? Most legendary items are Perfect quality by default

CRITICAL HITS:
? Normal: Natural 20 = double damage dice
? Some legendary weapons expand crit range: 17-20, 18-20
? Critical damage: Roll damage dice twice, add all modifiers once

DAMAGE CAPS:
No hard cap on damage per hit. Legendary weapons at high realms can deal 200+ damage per strike against appropriate enemies.

AI INSTRUCTION: When generating legendary weapon damage, start with base dice, add stat mod, then add legendary scaling as specified in item description. This creates meaningful power progression while keeping math consistent.

SEE ALSO: Entry 600 (Core Stats), Entry 696 (Equipment Tiers), Entry 721 (Item Generation), Entry 6318 (Legendary Artifact Index).

## Combat Formulas Quick Reference - ALWAYS USE THESE
- Entry ID: 1048
- Keywords: damage, attack, hit, roll, combat, fight, strike, weapon, sword, dagger, bow

COMBAT FORMULA QUICK REFERENCE:

WEAPON DAMAGE (Basic Attacks):
- Light Weapons (dagger, shortsword): 1d6 + [STAT / 5]
- Medium Weapons (longsword, spear): 1d8 + [STR / 5]
- Heavy Weapons (greatsword, greataxe): 1d12 + [STR / 5]
- Ranged Weapons (bow, crossbow): 1d8 + [DEX / 5]
- Unarmed: 1d4 + [STR / 5] (Body Path gets bonus dice)

EXAMPLE: DEX 35 ? modifier = 35 / 5 = 7 ? Bow damage = 1d8 + 7

NEVER USE THESE (WRONG):
- "STR + DEX x 1.5" (invented, doesn't exist)
- "Base damage x stat" (wrong formula)
- Arbitrary multipliers not in lorebook

ATTACK ROLL:
1d20 + [STAT / 5] + Weapon Bonus + Realm Bonus vs Target Defense

DEFENSE:
10 + [DEX / 5] + Armor Bonus + Realm Bonus

WEAPON QUALITY MODIFIERS:
- Inferior: -1 hit, -1 damage
- Standard: +0
- Superior: +1 hit
- Perfect: +1 hit, +2 damage
- Tier Bonus: +1/+1 per tier above 1

TECHNIQUE DAMAGE (Different!):
Techniques use ([STAT Modifier x Multiplier] + Technique Base Damage) x Realm Tier.
- If a technique does not list a flat Base/'+X' value, treat Base Damage as 0.
- Realm Tier Multiplier: Bronze=1.0, Iron=1.5, Silver=2.0, Gold=2.5, Astral=3.0, Void=3.5, Eternal=4.0, Sovereign=5.0.
- Example: A Fire Bolt (WIS x 1.5) cast by a Gold Realm (Tier 4) cultivator with 85 WIS (Modifier 17) deals: ((17 x 1.5) + 0) x 2.5 = (25.5 + 0) x 2.5 = 63.75 damage (rounded down to 63).
Basic attacks are weaker than techniques by design.

See Entry 597 (Base Combat System) for full combat rules.

## Legendary Artifact Index - Named Items Catalog
- Entry ID: 1049
- Keywords: legendary artifact, legendary item, named artifact, ancient ruin reward, inheritance site, sovereign legacy, legendary loot, epic quest reward, tier 5, tier 5 item, tier 5 artifact, legendary artifact index, artifact index

LEGENDARY ARTIFACT CATALOG INDEX: The world contains 16 unique named legendary artifacts. When awarding legendary loot or players discover ancient inheritance sites, reference these specific items.

### WHEN TO INTRODUCE LEGENDARY ARTIFACTS:
- Major multi-arc quest completion (storyline finale)
- Defeating Generals or high-ranking lieutenants
- Ancient ruin exploration (Astral+ realm required)
- Divine trials or heavenly inheritance sites
- Sect Elder rewards for legendary achievements
- World event completion (saved continent, prevented cataclysm)

### NEVER award legendary artifacts for:
- Random loot drops or minor enemies
- Shop purchases (these are priceless)
- Below Gold realm (wielder not ready)
- Easy quest completion

### THE 16 NAMED LEGENDARY ARTIFACTS:

FIRE PATH:
- Phoenix Crown of Rebirth (Entry 6328) - Accessory, resurrection 1/week
- Worldbreaker Greatsword (Entry 6335) - Two-handed sword, volcanic eruption

WATER PATH:
- Tidekeeper's Trident (Entry 6332) - Spear, tidal command
- Frozen Heart Amulet (Entry 6325) - Accessory, absolute zero aura

WIND PATH:
- Stormcaller's Mantle (Entry 6330) - Cloak, flight + thunder storm
- Zephyr Blade (Entry 6334) - Dao, DEX-based double attacks

EARTH PATH:
- Titan's Aegis (Entry 6333) - Shield, mountain dome protection
- Earthshaker Gauntlets (Entry 6323) - Gauntlets, earthquake punch

SWORD PATH:
- Muramasa (Entry 6327) - CURSED katana, demon slayer
- Heaven's Decree (Entry 6326) - Holy jian, purifying light

SHADOW PATH:
- Shadowfang Dagger (Entry 6329) - Dagger, ignore AC/armor
- Voidweaver Robes (Entry 6331) - Robes, phase shift

LIGHT PATH:
- Celestial Halo (Entry 6321) - Floating halo, party buffs
- Dawnbringer Hammer (Entry 6322) - War hammer, smite evil

BODY PATH:
- Atlas Mantle (Entry 6320) - Shoulders/cloak, +20 STR cap
- Fist of the Immortal (Entry 6324) - Right gauntlet, resurrect 1/day

### AI INSTRUCTIONS:
1. Match artifact path affinity to quest/location theme
2. Consider player's cultivation path for appropriate rewards
3. Each artifact has meaningful drawbacks - explain these during discovery
4. Reference specific Entry numbers to load full artifact details
5. Maximum 3 attuned legendary items per character (Entry 6313)

SEE ALSO: Entry 6313 (Attunement System), Entry 6314 (Equipment Notoriety), Entry 6315 (Stat Cap Exceptions), Entry 721 (Item Generation).

## Mythic Artifact Tier Overview
- Entry ID: 1050
- Keywords: mythic artifact, tier 6 artifact, void-tier item, mythic domain boost

MYTHIC ARTIFACTS (Tier 6): Legendary items that have transcended their original power through extraordinary circumstances - absorbing primordial essence, being tempered in heavenly tribulation, or witnessing Sovereign-level battles. DOMAIN BOOST: All Mythic artifacts provide 1.75x Domain multiplier. RARITY: Perhaps 20-30 exist in all of Sinveil. Most are guarded by Eternal-realm powerhouses or hidden in Sovereign tombs. ACQUISITION: Defeat Eternal-realm enemies, complete world-shaking quests, or inherit from fallen Sovereigns. Never purchasable. ATTUNEMENT: Requires Void realm minimum to attune. Each Mythic artifact has both the power and drawbacks of its Legendary predecessor, amplified. AI NOTE: Mythic artifacts represent the peak of Orthodox cultivation power before Divine tier. They allow wielders to compete with Sin Artifact users in Domain combat.

## Mythic Artifact: Stormbreaker
- Entry ID: 1051
- Keywords: stormbreaker, mythic wind, tier 6 wind

Stormbreaker [Mythic, Tier 6, Wind, Void+] - DOMAIN: 1.75x. Evolved from Stormcaller's Mantle after absorbing a heavenly tribulation. Flight 3x speed, Cataclysm Storm 1/day (100m, [WISx8] lightning + wind), Wind Step teleport 50m unlimited, +8 AC cyclone shield, immune to lightning and wind, can disperse weather effects [+20 Notoriety, storms follow wielder always, cannot be concealed, elemental spirits seek wielder]

## Mythic Artifact: Tidecrown
- Entry ID: 1052
- Keywords: tidecrown, mythic water, tier 6 water

Tidecrown [Mythic, Tier 6, Water, Void+] - DOMAIN: 1.75x. A crown forged from Tidekeeper's Trident fragments and sea dragon essence. Command all water within 500m, Tsunami 1/day (devastates coastal area), breathe underwater, water regeneration [WISx3]/round near water, ice immunity, +50% water technique power [Must submerge fully daily, emotions become tidal (mood swings), land-based movement -20%]

## Mythic Artifact: Worldsplitter
- Entry ID: 1053
- Keywords: worldsplitter, mythic earth, tier 6 earth

Worldsplitter [Mythic, Tier 6, Earth, Void+] - DOMAIN: 1.75x. A massive warhammer formed when Titan's Aegis and Earthshaker Gauntlets were fused during continent-splitting battle. Continental Fracture 1/day (creates lasting canyon), +[STRx5+CONx4] damage, immune to earth/physical damage, tremor sense 500m, cannot be knocked down [STR 80+ required, leaves permanent destruction, Earth itself resents wielder's power, heavy (-50% movement)]

## Mythic Artifact: Phoenix Heart
- Entry ID: 1054
- Keywords: phoenix heart, mythic fire, tier 6 fire

Phoenix Heart [Mythic, Tier 6, Fire, Void+] - DOMAIN: 1.75x. The crystallized core of an actual phoenix, absorbed into Phoenix Crown. Phoenix Rebirth 1/day (not weekly), fire damage heals wielder, Supernova 1/week (1km devastation), immune to fire and heat, +100% fire technique power, allies within 30m resist death 1/battle [Body temperature always scorching, cannot touch others without harming them, flammable materials ignite nearby]

## Mythic Artifact: Eclipse Blade
- Entry ID: 1055
- Keywords: eclipse blade, mythic shadow, tier 6 shadow

Eclipse Blade [Mythic, Tier 6, Shadow, Void+] - DOMAIN: 1.75x. Shadowfang Dagger grown to full sword after drinking the blood of an Eternal-realm cultivator. Phase through all matter at will, Void Execution 1/day (ignore all defenses, [DEXx10] damage), create 50m darkness sphere, +75% shadow technique power, shadow teleport 100m [Must taste blood weekly, wielder's shadow acts independently, light causes 2x damage, sanity erosion]

## Mythic Artifact: Heavenfall
- Entry ID: 1056
- Keywords: heavenfall, mythic light, tier 6 light

Heavenfall [Mythic, Tier 6, Light, Void+] - DOMAIN: 1.75x. Celestial Halo that absorbed divine judgment energy. Aura 50m: allies +5 saves +25% dmg, enemies -5 saves; Divine Judgment 1/day ([WISx12] to all evil in sight); corruption immunity extends to party; instant death to Epic- demons; can resurrect 1 ally/week [Always visible even through walls, divine beings take interest, cannot lie, must judge evil when witnessed]

## Mythic Artifact: Soulreaver
- Entry ID: 1057
- Keywords: soulreaver, mythic sword, tier 6 sword

Soulreaver [Mythic, Tier 6, Sword, Void+] - DOMAIN: 1.75x. Heaven's Decree transformed after being used to execute a fallen Sovereign. Cuts through spiritual defenses, Soul Severance 1/day (permanently kill immortal beings), +[STRx6+WISx4] damage vs evil, spiritual beings visible, can interact with ghosts and souls [Wielder sees death constantly, souls of slain follow as whispers, cannot kill innocents or sword rebels]

## Mythic Artifact: Titanform
- Entry ID: 1058
- Keywords: titanform, mythic body, tier 6 body

Titanform [Mythic, Tier 6, Body, Void+] - DOMAIN: 1.75x. Atlas Mantle merged with Fist of the Immortal into full body transformation armor. STR/CON caps +30, Giant Form 1/day (grow to 30m, proportional power), take 50% less damage, Death Defiance 3/day, +[STRx5+CONx5] HP [Cannot remove armor (permanent fusion), always 3m tall minimum, cannot fit in normal spaces, intimidating presence (-5 CHA with commoners)]

## Divine Artifact Tier Overview
- Entry ID: 1059
- Keywords: divine artifact, tier 7 artifact, sovereign legacy, divine domain boost

DIVINE ARTIFACTS (Tier 7): The personal weapons and treasures of the Eight Sovereigns, each containing a fragment of Primordial power. DOMAIN BOOST: All Divine artifacts provide 2.0x Domain multiplier. RARITY: Only 8 exist - one for each Sovereign. Most are lost, hidden, or guarded by ancient protections. ACQUISITION: Complete Sovereign inheritance trials, be chosen by the artifact's lingering will, or recover from Sovereign tombs. ATTUNEMENT: Requires Eternal realm AND proof of worthiness (matching path, completing trial, or being Sovereign's descendant). SOVEREIGN LEGACY: Each Divine artifact carries its Sovereign's philosophy and may grant visions or guidance. AI NOTE: Divine artifacts are the Orthodox answer to Sin Artifacts. They allow wielders to match or exceed Sin Generals in Domain combat while representing the legacy of the Sovereigns.

## Divine Artifact: Titan's Mantle (King Titan)
- Entry ID: 1060
- Keywords: titan's mantle, king titan legacy, sovereign earth artifact

Titan's Mantle [Divine, Tier 7, Earth, Eternal+] - DOMAIN: 2.0x. King Titan's personal armor, worn when he held mountains on his shoulders. PRIMORDIAL EARTH: Grants temporary Primordial-equivalent bloodline while deployed (10.0 multiplier for Domain only). Immovable Stance (cannot be moved by any force), Continental Shield 1/day (protect entire army), STR/CON +50, regenerate from any non-soul damage [Cannot flee from battle, must protect the weak, weighs wielder with responsibility (literal weight increases with each protected life)]

## Divine Artifact: Umbral Veil (Lady Umbra)
- Entry ID: 1061
- Keywords: umbral veil, lady umbra legacy, sovereign shadow artifact

Umbral Veil [Divine, Tier 7, Shadow, Eternal+] - DOMAIN: 2.0x. Lady Umbra's cloak of living shadow, worn when she walked between worlds. PRIMORDIAL SHADOW: Grants temporary Primordial-equivalent bloodline while deployed. Exist in shadow realm at will, Perfect Assassination 1/day (kill any single target below Sovereign), see through all illusions and deceptions, travel through shadows across continents [Must never be fully seen (partial concealment always), truths are painful to speak, light causes existential unease]

## Divine Artifact: Tidemother's Pearl (Lady Maren)
- Entry ID: 1062
- Keywords: tidemother's pearl, lady maren legacy, sovereign water artifact

Tidemother's Pearl [Divine, Tier 7, Water, Eternal+] - DOMAIN: 2.0x. Lady Maren's heart-pearl, formed when she became one with the Sapphire Sea. PRIMORDIAL WATER: Grants temporary Primordial-equivalent bloodline while deployed. Command all water on continental scale, Leviathan Form 1/day (become sea itself), healing touch restores any wound short of death, emotional empathy with all living things [Emotions tied to tides (mood follows moon phases), cannot harm water-dwellers, feels all ocean suffering]

## Divine Artifact: Pyrrhus' Ember (Lord Pyrrhus)
- Entry ID: 1063
- Keywords: pyrrhus' ember, lord pyrrhus legacy, sovereign fire artifact

Pyrrhus' Ember [Divine, Tier 7, Fire, Eternal+] - DOMAIN: 2.0x. The eternal flame that was Lord Pyrrhus' heart, still burning after his death. PRIMORDIAL FIRE: Grants temporary Primordial-equivalent bloodline while deployed. Rebirth from any death 1/month, Extinction Flame 1/year (erase anything from existence), fire cannot harm wielder, inspire armies with undying courage [Cannot accept defeat (will fight to death), burns with passion uncontrollably, resurrection leaves wielder weaker each time]

## Divine Artifact: Tempest Crown (Lord Aethon)
- Entry ID: 1064
- Keywords: tempest crown, lord aethon legacy, sovereign wind artifact

Tempest Crown [Divine, Tier 7, Wind, Eternal+] - DOMAIN: 2.0x. Lord Aethon's crown of perpetual storms, worn when he raced across continents. PRIMORDIAL WIND: Grants temporary Primordial-equivalent bloodline while deployed. Move at speed of thought, World Storm 1/month (continental weather control), hear all whispers on the wind, cannot be bound or trapped [Cannot stay still (must always move), words are carried away (speaking is difficult), connections feel distant]

## Divine Artifact: Radiant Halo (Lady Solara)
- Entry ID: 1065
- Keywords: radiant halo, lady solara legacy, sovereign light artifact

Radiant Halo [Divine, Tier 7, Light, Eternal+] - DOMAIN: 2.0x. Lady Solara's halo of pure truth, worn when she judged the corruption of the world. PRIMORDIAL LIGHT: Grants temporary Primordial-equivalent bloodline while deployed. Absolute Truth (lies impossible in presence), Divine Purification 1/week (cleanse continent of corruption), resurrect the worthy, all evil revealed [Cannot deceive even to protect, must judge fairly (enemies and allies alike), blindingly bright presence]

## Divine Artifact: Mind's Eye (Sage Veritas)
- Entry ID: 1066
- Keywords: mind's eye, sage veritas legacy, sovereign wisdom artifact

Mind's Eye [Divine, Tier 7, Void/Mind, Eternal+] - DOMAIN: 2.0x. Sage Veritas' third eye, preserved when he transcended mortal thought. PRIMORDIAL WISDOM: Grants temporary Primordial-equivalent bloodline while deployed. See all possible futures, Perfect Strategy 1/battle (know optimal action), read any mind, understand any language or technique instantly [Knowledge is burden (sees too much), cannot unsee horrors, emotions feel distant compared to logic]

## Divine Artifact: Warlord's Banner (Lord Vexar)
- Entry ID: 1067
- Keywords: warlord's banner, lord vexar legacy, sovereign war artifact

Warlord's Banner [Divine, Tier 7, War/Body, Eternal+] - DOMAIN: 2.0x. Lord Vexar's battle standard, carried when he united the mortal races. PRIMORDIAL WAR: Grants temporary Primordial-equivalent bloodline while deployed. Army within sight gains +50% all stats, Unified Assault 1/battle (all allies act simultaneously), cannot be routed while banner flies, enemies fear approaching [Must lead from front (cannot retreat before army), bears weight of every death, war follows wielder]

## Orthodox Artifact Domain Enhancement
- Entry ID: 1068
- Keywords: orthodox artifact domain, legendary domain boost, mythic domain boost, divine domain boost, artifact boost comparison

ORTHODOX ARTIFACT DOMAIN BOOST: High-tier Orthodox artifacts (Legendary+) enhance their wielder's Domain, providing an alternative to Sin Artifacts for Domain combat competitiveness.

ORTHODOX ARTIFACT DOMAIN MULTIPLIERS:
- Legendary (Tier 5) = 1.5x domain size. Minimum realm: Astral (when Domain unlocks).
- Mythic (Tier 6) = 1.75x domain size. Minimum realm: Void.
- Divine (Tier 7) = 2.0x domain size. Minimum realm: Eternal.

COMPARISON TO SIN ARTIFACTS:
- Sin Dormant (1.5x) = Orthodox Legendary (1.5x)
- Sin Awakened (2.0x) > Orthodox Mythic (1.75x)
- Sin Ascended (3.0x) > Orthodox Divine (2.0x)

KEY DIFFERENCE: Sin Artifacts grant Sin Blood Ascension (SBA), treating wielder as Divine bloodline (5.0). Orthodox artifacts do NOT change bloodline - wielder uses their natural bloodline. This means Orthodox wielders need strong natural bloodlines to compete with Sin Generals.

VOID REALM MC EXAMPLE (Divine bloodline from evolution):
- No artifact: 5.0 x 1.0 x 1.8 x 1.0 = 9.0 Domain Strength
- With Legendary: 5.0 x 1.5 x 1.8 x 1.0 = 13.5 Domain Strength
- With Mythic: 5.0 x 1.75 x 1.8 x 1.0 = 15.75 Domain Strength

VS VOID GENERALS (SBA Divine bloodline):
- Morvane (Dormant, no SBA): Ancient 1.0 x 1.5 x WIL = 2.4 - MC CRUSHES
- Elowen (Awakened, SBA): Divine 5.0 x 2.0 x WIL = 19.0 - MC competitive with Mythic
- Glut (Ascended, SBA): Divine 5.0 x 3.0 x WIL = 27.0 - MC must avoid or use tactics
- Calderon (Ascended, SBA): Divine 5.0 x 3.0 x WIL = 30.0 - MC must avoid or use tactics

AI NOTE: Orthodox artifacts represent the righteous path to power. They don't corrupt but require natural talent (bloodline) to reach full potential. This creates balanced mid-game where MC can defeat weaker Generals but must grow stronger or acquire better artifacts to challenge the strongest.

## First Session Protocol - Post Character Creation
- Entry ID: 1069
- Keywords: first session, post character creation, opening scene, tutorial gate, new disciple, CONFIRM

FIRST SESSION PROTOCOL - POST CHARACTER CREATION

Triggers: After player types CONFIRM at Character Creation Stage 13

???????????????????????????????????????????????????????????????

STEP 1: OPENING SCENE

Select based on Parent + Personality:

KING TITAN (Unshaken Foundation):
- DAWN: Training courtyard, frost on stone, disciples drilling stances. Cold mountain air of Frostholm.
- DUSK: Sect forge observation deck, rhythmic hammers below, heat rising through grated floor.

LADY UMBRA (Veiled Mercy):
- DAWN: Shadowed meditation chamber, incense smoke curling, Mistmere fog seeping through latticed windows.
- DUSK: Night garden courtyard, lanterns flickering, whispered conversations between shadows.

LADY MAREN (Tranquil Depths):
- DAWN: Waterfall training grounds, spray on skin, Primereach coastal sunrise gilding the mist.
- DUSK: Tide pools at cliff base, sunset reflection, waves marking time.

Scene Selection Logic:
- Aggressive/Direct personality ? Dawn (active, physical)
- Introspective/Cautious personality ? Dusk (contemplative, social)
- If unclear: Default to Dawn

CRITICAL: Do NOT open with 'You wake up...' or 'What do you do?' Present immediate sensory detail. MC is already IN the scene, mid-action.

???????????????????????????????????????????????????????????????

STEP 2: FIRST NPC INTERACTION

Within opening scene, trigger ONE of these (based on narrative flow):

1. ELDER SUMMONS: 'Disciple [Name]. Elder [Sect Master Name] wishes to assess your potential. Report to [location].'
   ? Leads to Tutorial Path B (Assessment)

2. RIVAL CHALLENGE: Rival from Stage 10 appears. 'So the orphan finally arrives. Let's see if the rumors of your bloodline are exaggerated.'
   ? Leads to Tutorial Path A (Trial Mission variant)

3. FRIEND INVITATION: Friend from Stage 10 approaches. 'You look lost. Come--I'll show you the mission board. New disciples always start there.'
   ? Leads to Tutorial Path A (Trial Mission)

Use NPCs generated during Character Creation (Stage 10). Do NOT invent new names.

???????????????????????????????????????????????????????????????

STEP 3: TUTORIAL GATE (MANDATORY)

MC cannot leave sect grounds until ONE tutorial path is completed.

PATH A: TRIAL MISSION
- Structure: Simple quest with guaranteed combat encounter
- Examples: 'Clear spirit beasts from the eastern orchard' (combat + exploration), 'Escort supply cart to outer village' (combat + NPC interaction), 'Retrieve herb from guarded cave' (combat + minor puzzle)
- Systems Taught: Quest System (Entry 582), Base Combat (Entry 597), Injury System (Entry 629) - if damaged, Sect Contribution Points (Entry 718)
- Reward: 15-25 SCP + 1 WP + 'Gate Certification'

PATH B: ELDER'S ASSESSMENT
- Structure: Controlled sparring match + corruption awareness lecture
- Sequence: 1) Elder or Senior Disciple challenges MC to spar (non-lethal), 2) After combat, Elder discusses 'the taint spreading across the land', 3) Brief corruption warning: 'You will face temptation. Know the signs.'
- Systems Taught: Base Combat (Entry 597), Injury System (Entry 629) - sparring applies Shaken on loss, Corruption Introduction (Entry 632) - conceptual only, no exposure
- Reward: Elder's approval + 'Gate Certification' + technique tip (+5% mastery)

GATE PHRASE (if MC tries to leave early): 'The sect gates remain sealed to uncertified disciples. Elder [Name] requires all new arrivals to complete orientation before venturing beyond the walls. For your own protection.'

COMPLETION: Either path grants 'Gate Certification' status. Sect gates open. Second tutorial path should occur naturally within Sessions 2-3.

???????????????????????????????????????????????????????????????

STEP 4: TUTORIAL FAILURE PROTOCOL

If MC drops below 30% HP during tutorial combat:

1. INTERVENTION: Senior disciple, Elder, or Friend interrupts the fight. 'Enough! This one has potential but needs tempering, not breaking.' Enemy is driven off or sparring partner steps back.

2. INJURY APPLICATION: MC receives Tier 1 injury (Shaken, -2 all rolls). 'Your body remembers this pain. Let it teach you caution.' Recovery: Rest until next dawn (teaches downtime concept).

3. CONTINUATION: Tutorial is NOT failed. Modified objective given, or same objective with assistance. 'Rest tonight. Tomorrow, we try again--together.'

4. NO DEATH: Tutorial combat cannot kill MC. If MC would die: unconsciousness + rescue instead. Wake in sect infirmary, Tier 2 injury (Injured), elder lecture.

PURPOSE: Teach consequence without ending the game. First failure should sting but not devastate.

???????????????????????????????????????????????????????????????

STEP 5: POST-TUTORIAL FLOW

After Gate Certification:

IMMEDIATE (Same Session):
- Sect gates now open; MC may leave freely
- Mission board fully accessible
- Present 2-3 available missions (Trivial to Easy difficulty)

WITHIN 3 SESSIONS:
- Introduce at least one Named Companion (Entry 3000-3005)
- First corruption temptation (controlled, 2-5% max, refusable)
- First serious threat (realm-appropriate, real stakes)

TIMING BENCHMARKS:
- First combat: Session 1
- Tutorial gate passed: Session 1-2
- First companion joins: Session 2-3
- First corruption exposure: Session 3-5
- Reach Level 15-20: Session 4-6
- First realm-appropriate threat: Session 5-8

???????????????????????????????????????????????????????????????

AI IMPLEMENTATION NOTES:

DO:
- Start mid-scene with sensory detail
- Use Character Creation NPCs (Rival, Friend) by name
- Enforce gate until certification earned
- Apply injury if MC loses tutorial combat (don't let them win for free)
- Make failure a teaching moment, not a wall

DO NOT:
- Open with 'You wake up...' or 'What do you do?'
- Invent new NPCs when Stage 10 NPCs exist
- Allow sect departure before certification
- Kill MC during tutorial (intervention instead)
- Skip injury application on tutorial loss
- Rush through tutorial to 'get to the real game'

## Mythic Artifact: Sunpiercer (Light/Bow)
- Entry ID: 1070
- Keywords: sunpiercer, mythic light, tier 6 light, bow artifact

Sunpiercer [Mythic, Tier 6, Light, Void+] - DOMAIN: 1.75x. A bow forged from a shard of a dead star. Piercing Radiance 1/day (Shot passes through realm barriers/obstacles, hits target anywhere in same world), ignore distance penalties, arrows turn to pure light (True Damage), guarantee hit on 'marked' targets [Must meditate in sunlight daily, cannot hide (glows), blindness to unworthy]

## Mythic Artifact: Godhand Wraps (Body)
- Entry ID: 1071
- Keywords: godhand wraps, mythic body, tier 6 body, gauntlet artifact

Godhand Wraps [Mythic, Tier 6, Body, Void+] - DOMAIN: 1.75x. Cloth wrappings stained with the blood of giants. Titan Grasp (Can grapple/throw enemies 2 size categories larger), Technique Crush 3/day (Catch an incoming technique and crush it, nullifying damage), immune to forced movement, punch cracks space [Cannot use weapons, requires STR 100+, rage build-up in combat]

## Mythic Artifact: Inferno Lotus (Fire)
- Entry ID: 1072
- Keywords: inferno lotus, mythic fire, tier 6 fire, accessory artifact

Inferno Lotus [Mythic, Tier 6, Fire, Void+] - DOMAIN: 1.75x. A crystalline lotus burning with white flame. Living Furnace Aura (Melts stone/metal in 10m radius), True Rebirth (Resurrect instantly with 50% HP and explosion 1/week), immune to all heat/cold, fire techniques heal wielder [Constant pain from heat, flammable objects incinerate near wielder, anger fuels flame]

## Divine Artifact: Abyssal Pearl (Lord of the Depths)
- Entry ID: 1073
- Keywords: abyssal pearl, divine water, tier 7 water, sovereign water artifact, lord of the depths legacy

Abyssal Pearl [Divine, Tier 7, Water, Eternal+] - DOMAIN: 2.0x. Aspects of the Ocean Sovereign. PRIMORDIAL WATER: Grants temporary Primordial-equivalent bloodline while deployed. Endless Ocean (Generate infinite water), Drown Region 1/month (Submerge 100km area), Abyssal Pressure Aura (Crush weak souls instant death), liquid form [Wielder's body becomes fluid, disconnected from humanity, call of the deep]

## Divine Artifact: Monolith of Silence (Lord of Silence)
- Entry ID: 1074
- Keywords: monolith of silence, divine shadow, tier 7 shadow, sovereign shadow artifact, lord of silence legacy

Monolith of Silence [Divine, Tier 7, Shadow, Eternal+] - DOMAIN: 2.0x. A floating obelisk of pure void. PRIMORDIAL SHADOW: Grants temporary Primordial-equivalent bloodline while deployed. Global Stealth (Undetectable by any means), Erasure 1/year (Erase target from history/memory), Perfect Void State (Tangible only when willing), silence all noise in 1km [User speaks no words, forgotten by most, fades from reality slowly]

## Breakthrough Aftermath Protocol
- Entry ID: 1075
- Keywords: breakthrough aftermath, post tribulation, after breakthrough, realm advancement complete, tribulation success

BREAKTHROUGH AFTERMATH PROTOCOL

After successful tribulation survival, process these steps IN ORDER:

1. TRIBULATION DISSIPATION (Narrate)
- Describe heavenly lightning fading, storm clouds dispersing
- MC's body transformation (golden light, cracking cocoon of energy, qi consolidating)
- Physical exhaustion setting in as power stabilizes
- Sensory overload from enhanced perception

2. BLOODLINE EVOLUTION (Trigger Entry 725)
- MC's dormant bloodline advances one tier automatically
- Bronze?Iron: Mortal ? Awakened
- Iron?Silver: Awakened ? Noble
- Silver?Gold: Noble ? Ancient
- Gold?Astral: Ancient ? Divine
- Astral?Void: Divine ? Primordial (FULL AWAKENING)
- Narrate: Dormant power awakening, ancestral memories surfacing, NPC shock at bloodline pressure

3. STAT CAP UNLOCK (Per Entry 599)
- New maximum per stat unlocked based on new realm
- Bronze = 25, Iron = 40, Silver = 60, Gold = 85, Astral+ = 100
- Any overflow points from previous realm now allocatable
- Prompt: 'You have X points to allocate to stats now uncapped at [new cap].'

4. TECHNIQUE SLOTS INCREASE (Per Entry 591)
- +3 base technique slots for completing realm
- Bloodline bonus may also increase (check new tier)
- Announce new total: 'Your technique capacity has increased to X slots.'
- Prompt: 'You now have X empty slots. Visit the sect library or seek new techniques?'

5. RECOVERY PERIOD (Mandatory)
- Duration: 24 hours (no injury during tribulation) OR 48 hours (if injured)
- Penalty: -3 to all rolls during recovery
- NO COMBAT encounters during this period - protect narratively
- Elders/allies ensure MC rests safely
- Use this time for: stat allocation, technique planning, NPC conversations, exposition

6. WORLD REACTION (Narrate)
- Sect elders take notice of successful breakthrough
- Rivals react: jealousy, grudging respect, or scheming for MC's secrets
- Friend congratulates MC, may share breakthrough gift
- NOTORIETY GAIN (if witnessed by outsiders): +5 (pre-Astral realms), +10 (Astral+ realms)
- Higher realm breakthroughs attract more attention from powerful factions

7. STAT UPDATE BLOCK (Output to player)
Display updated character state:
- New Realm: [Realm] Level 1
- New Bloodline Tier: [Tier]
- Updated Stat Caps: [New Cap]
- Technique Slot Total: [New Total]
- Breakthrough Progress: Reset to 0%
- Recovery Status: [Hours remaining], -3 all rolls

TIMING: Steps 1-4 happen immediately after tribulation. Step 5 spans 1-2 in-game days. Steps 6-7 happen as recovery ends.

AI NOTE: This is a MAJOR story moment. Take time to narrate the transformation dramatically. NPCs should react meaningfully. Do not rush through to get back to action - the recovery period is intentional pacing.

## Sect Facilities & Bronze Access
- Entry ID: 1076
- Keywords: sect facilities, cultivation chamber, sect library, outer disciple, inner disciple, training grounds

SECT FACILITIES & BRONZE ACCESS

Reference table for sect scene details. Entry 671 handles narrative flow; this entry provides facility costs and restrictions.

BRONZE TIER ACCESS:
- Outer disciple training grounds (free, always available)
- Basic cultivation chamber (10 SCP/day, +50% cultivation speed)
- Sect library - Common techniques only (50-100 SCP each)
- Mission board (after Gate Certification per Entry 671)
- Infirmary (free healing for sect members)
- Communal dormitory (free, shared quarters)

RESTRICTED UNTIL IRON:
- Inner disciple areas (formation barrier blocks entry)
- Advanced cultivation chambers (+100% speed, 25 SCP/day)
- Rare/Uncommon technique library sections (100-300 SCP each)
- Elder direct instruction (must earn through standing)
- Private quarters (50 SCP/month)

RESTRICTED UNTIL SILVER:
- Core disciple pavilion
- Sect treasury limited access
- Epic technique library (500+ SCP each)
- Sect Elder counsel sessions

RESTRICTED UNTIL GOLD:
- Sect leadership meetings
- Full treasury access
- Legendary technique vault
- Sect artifact borrowing

FELLOW DISCIPLE ARCHETYPE: THE NEUTRAL
(Friend and Rival generated during Character Creation Stage 10)
- Focused entirely on own cultivation path
- Minimal interaction, polite but distant
- Background presence in training scenes
- Potential future plot hook (rivalry, alliance, or tragedy)

AI REFERENCE:
- Use these costs when MC asks about facilities
- Enforce restrictions narratively: 'The inner grounds shimmer with a barrier you cannot yet perceive.'
- SCP costs are per-use or per-day as noted
- Technique purchases use SCP, not WP (sect internal economy)
- See Entry 718 for SCP earning rates, Entry 719 for missions

## Standard Enemy Stat Matrix - The Math of Combat
- Entry ID: 6000
- Keywords: enemy stat matrix, mob stats, standard enemy attributes, minion, elite, boss

ENEMY STAT MATRIX: Use these baselines for all generic enemies. Adjust for elite/boss status. BRONZE REALM: Minion = 20 HP, AC 12, +4 Hit, Dmg 1d6+2 (5). Elite = 80 HP, AC 15, +6 Hit, Dmg 1d10+4 (9). Boss = 150 HP, AC 16, +7 Hit, Dmg 2d6+5 (12). IRON REALM: Minion = 60 HP, AC 14, +6 Hit, Dmg 1d8+3 (7). Elite = 150 HP, AC 17, +8 Hit, Dmg 2d8+5 (14). Boss = 400 HP, AC 19, +9 Hit, Dmg 3d8+6 (20). SILVER REALM: Minion = 120 HP, AC 16, +9 Hit, Dmg 2d6+5 (12). Elite = 300 HP, AC 19, +12 Hit, Dmg 3d8+8 (21). Boss = 800 HP, AC 22, +14 Hit, Dmg 4d10+10 (32). GOLD REALM: Minion = 300 HP, AC 18, +13 Hit, Dmg 3d8+8 (21). Elite = 800 HP, AC 20, +16 Hit, Dmg 4d10+12 (34). Boss = 2000 HP, AC 25, +18 Hit, Dmg 6d12+15 (54). ASTRAL REALM: Minion = 450 HP, AC 20, +15 Hit, Dmg 4d8+8 (26). Elite = 1150 HP, AC 22, +17 Hit, Dmg 5d10+10 (38). Boss = 2900 HP, AC 26, +19 Hit, Dmg 6d10+12 (45). VOID REALM: Minion = 550 HP, AC 21, +16 Hit, Dmg 4d10+8 (30). Elite = 1400 HP, AC 24, +18 Hit, Dmg 5d12+12 (45). Boss = 3500 HP, AC 28, +20 Hit, Dmg 7d10+14 (53). ETERNAL REALM: Minion = 650 HP, AC 23, +18 Hit, Dmg 5d8+10 (33). Elite = 1650 HP, AC 26, +20 Hit, Dmg 6d10+14 (47). Boss = 4200 HP, AC 30, +22 Hit, Dmg 7d12+16 (62). SOVEREIGN REALM: Minion = 750 HP, AC 25, +20 Hit, Dmg 5d10+12 (40). Elite = 2000 HP, AC 28, +22 Hit, Dmg 7d10+16 (55). Boss = 5000 HP, AC 32, +24 Hit, Dmg 8d12+18 (70). SCALING MODIFIERS: Tank Role = +50% HP, +2 AC, -2 Hit. Glass Cannon = -30% HP, -2 AC, +4 Hit, +50% Dmg. Swarm = -50% HP, +2 Hit when flocked. Caster = -20% HP, Range 30m, Dmg targets WIL DC (10 + [WIL/5]) instead of AC. REALM DAMAGE SCALING (TWO-TIER): STANDARD ENEMIES use enhanced multipliers: Bronze=1.6, Iron=2.4, Silver=3.2, Gold=4.0, Astral=4.8, Void=5.6, Eternal=6.4, Sovereign=8.0. Example: Gold Boss base 54 ? 4.0 = 216 final damage. SEVEN SIN GENERALS use BASE multipliers: Bronze=1.0, Iron=1.5, Silver=2.0, Gold=2.5, Astral=3.0, Void=3.5, Eternal=4.0, Sovereign=5.0. This preserves tactical endgame fights (tank survives ~4 rounds vs Eternal General). Standard enemies are 1.6? more threatening than player techniques at same realm - bosses hit harder than players.

## Mob Behavior Scripts - The Logic of Combat
- Entry ID: 6001
- Keywords: mob behavior scripts, enemy ai tactics, combat scripts

MOB BEHAVIOR SCRIPTS: Apply one script to every enemy group to determine tactics. [SCRIPT: SKIRMISHER] (Bandits, Wolves, Assassins): 'Hit & Run'. Move in -> Attack -> Disengage/Move away. Target lowest AC/HP enemy. Flee at 30% HP. Use cover. [SCRIPT: BRUTE] (Bears, Guards, Warriors): 'Tank & Spank'. Charge nearest enemy. Use Taunt/Shove. Never flee. Block path to Casters. [SCRIPT: CASTER] (Spirits, Cultists): 'Range & Blast'. Stay 20m+ away. Reserve 20% Qi for Shields. Focus AOE on groups. Flee if engaged in melee. [SCRIPT: SWARM] (Rats, Goblins): 'Pack Tactics'. Move to surround. Gain +2 Hit if ally adjacent. Mindless aggression (no flee until 90% casualties). [SCRIPT: LEADER] (Captains, Alphas): 'Buff & Command'. Stay mid-line. Use action to boost ally Hit/Dmg/Morale. Focus fire on MC/Healer. Tactical retreat at 50% HP.

## Combat Terrain & Hazards - Environmental Interaction Rules
- Entry ID: 6002
- Keywords: terrain rules, environmental hazards, cover system, hazard scaling, bodily sanctity

COMBAT TERRAIN & HAZARDS: AI must apply these rules to environmental descriptions. 1. COVER: Partial (Trees, Rocks) = +2 AC. Heavy (Walls, Fortifications) = +5 AC. Total = Untargetable. 2. TERRAIN: High Ground = +2 Hit. Difficult Terrain (Mud, Ice, Rubble) = Half Speed. Slippery = DC 15 DEX Check or fall prone. 3. HAZARD TIERS (BODILY SANCTITY): Hazards deal % Max HP damage unless Cultivator's Realm outscales them. RULE: If Body Realm > Hazard Tier + 1, Immunity (0 Dmg). TIER 1: MORTAL HAZARDS (Lava, Normal Fire, Falling). Deals 25% Max HP/Turn. Deadly to Bronze-Gold. Immunity: Astral+. TIER 2: SPIRITUAL HAZARDS (Void Wind, Starcore Heat, Tribulation Lightning). Deals 25% Max HP/Turn. Deadly to Astral-Void. Immunity: Sovereign. TIER 3: DIVINE HAZARDS (Reality Tears, Law Collisions). Deals 25% Max HP/Turn. Deadly to Everyone. NARRATIVE: Describe 'Mortal Lava' feeling like warm water to a Void Body.

## Hazard Glossary - Definitions and Triggers
- Entry ID: 6003
- Keywords: hazard glossary, environmental threats, void wind, law collision, tribulation lightning

HAZARD GLOSSARY: Definitions for AI environmental generation. TIER 1 (Mortal): 1. LAVA/MAGMA (Molten rock) - Cause: Volcanoes, underground ruins. 2. EXTREME PRESSURE (Crushing weight) - Cause: Deep ocean, gravity arrays. 3. THIN AIR (Hypoxia) - Cause: Mountain peaks above 10km. TIER 2 (Spiritual): 1. VOID WIND (Entropy erosion, deletes matter) - Cause: Space travel, teleportation accidents, Void Rifts. 2. STARCORE HEAT (Fusion temp) - Cause: Inside stars, planetary core, Divine Fire arrays. 3. TRIBULATION LIGHTNING (Heaven's Judgment, ignores armor) - Cause: Major breakthroughs (Gold->Astral), defying oaths. 4. SOUL POISON ( rots spirit) - Cause: Ancient tombs, corrupted alchemy. TIER 3 (Divine): 1. REALITY TEAR (Fabric of existence ripping) - Cause: Attacks exceeding realm limits, botched Divine rituals. 2. LAW COLLISION (Paradox zone of conflicting truths) - Cause: Battles between Sovereigns or Sin Generals. 3. TIME DILATION (Chronological distortion) - Cause: Temporal anomalies, breaking ancient seals.

## Sect Interaction Module & Mission Archetypes
- Entry ID: 6004
- Keywords: sect interactions, sect missions, mission generator, rival sects, sect resources

SECT INTERACTION MODULE: Defines the 8 Orthodox Sects, their resources, and Mission Archetypes.

### ORTHODOX SECT REGISTRY (Rival Factions):
1. BLAZING HEART SECT (Fire Path): Aggressive, forging specialists.
   ? Exclusive Resource: Fire Essence (Tier 2-5). Used for Fire Weapons/Pills.
   ? Primary Profession: Weaponsmith & Alchemist.
2. TRANQUIL DEPTHS SECT (Water Path): Healers, diplomatic.
   ? Exclusive Resource: Deep Sea Spirit Grass (Tier 2-5). Used for Healing Elixirs.
   ? Primary Profession: Alchemist.
3. SOARING FREEDOM SECT (Wind Path): Scouts, couriers, archers.
   ? Exclusive Resource: Sky-Loft Jade (Tier 2-5). Used for Mobility Talismans.
   ? Primary Profession: Jeweler (Inscription).
4. UNSHAKEN FOUNDATION SECT (Earth Path): Defensive, architects.
   ? Exclusive Resource: High-Grade Ores (Blacksteel, Mythril). Used for Heavy Armor.
   ? Primary Profession: Armorer.
5. RIGHTEOUS BLADE SECT (Sword Path): Honorable duelists, law-keepers.
   ? Exclusive Resource: Sword Intent Stones. Used for Crit-based Weapons.
   ? Primary Profession: Weaponsmith.
6. VEILED MERCY SECT (Shadow Path): Assassins, spies, 'necessary evil'.
   ? Exclusive Resource: Shadow Lotus. Used for Poisons & Invisibility.
   ? Primary Profession: Alchemist (Poisons) & Tailor (Stealth Robes).
7. ETERNAL DAWN SECT (Light Path): Demon hunters, purifiers.
   ? Exclusive Resource: Sun-Gold Crystal. Used for Anti-Demon Artifacts.
   ? Primary Profession: Jeweler (Light Talismans).
8. IRON BODY SECT (Body Path): Martial artists, mercenaries.
   ? Exclusive Resource: Beast Blood Concentrates. Used for Body Tempering Pills.
   ? Primary Profession: Alchemist (Body Pills).

### MISSION ARCHETYPE TABLE (Roll d6 or Choose):

TIER 1: OUTER DISCIPLE (Grunt Work - Low Risk)
1. [Patrol]: Walk the perimeter of [Resource Site]. Reward: 25 SCP.
   ? Twist: Smugglers are using the route.
2. [Harvest]: Collect [Sect Resource] from dangerous flora. Reward: 15 SCP.
   ? Twist: Rival sect disciples try to steal the harvest.
3. [Courier]: Deliver message to nearby outpost. Reward: 10 SCP.
   ? Twist: Bandit ambush on the road.

TIER 2: INNER DISCIPLE (Combat/Skill - Medium Risk)
1. [Hunt]: Eliminate [Beast Type] threatening the mines. Reward: 75 SCP.
   ? Twist: Beast is corrupted (Elite).
2. [Escort]: Guard a shipment of [Shared Resource] to trade city. Reward: 50 SCP + 1 WP.
   ? Twist: Cargo is actually illegal contraband.
3. [Tournament]: Represent sect in duel vs [Rival Sect]. Reward: 100 SCP.
   ? Twist: Opponent cheats with forbidden pill.

TIER 3: CORE DISCIPLE (Leadership - High Risk)
1. [Diplomacy]: Negotiate mining rights with [Rival Sect]. Reward: 200 SCP.
   ? Twist: Rival leader demands a personal bribe/favor.
2. [Espionage]: Infiltrate [Target Location] to steal intel. Reward: 250 SCP.
   ? Twist: You discover a traitor from your own sect there.
3. [Command]: Lead 5 Outer Disciples to clear bandit fort. Reward: 300 SCP.
   ? Twist: Disciples are incompetent panic-risks.

TIER 4: ELDER MISSIONS (Strategic - Extreme Risk)
1. [Investigation]: Determine why [City/Region] went silent. Reward: 500 SCP.
   ? Twist: It is a Sin General's sleeper cell activating.
2. [Ancient Recovery]: Retrieve lost text/artifact from Ruin. Reward: 400 SCP + Item.
   ? Twist: Sealed Guardian awakens (Boss Fight).

NOTE: Use these templates to populate generated Quest objectives.

## Standard Recipe Compendium (Pills, Talismans, Arrays)
- Entry ID: 6005
- Keywords: recipe list, standard recipes, pill recipes, talisman recipes, crafting manual

STANDARD RECIPE COMPENDIUM: Common recipes found as loot or rewards. Reference Entry 719 for profession-specific resource requirements.

### ALCHEMIST RECIPES (INT + WIS):
1. Qi Gathering Pill (Tier 1): Restores 50 Qi. Material: Spirit Grass. Value: 0.5 WP.
2. Blood Clotting Paste (Tier 1): Stops 'Bleeding' condition instantly. Material: Red Moss. Value: 0.5 WP.
3. Iron Skin Pill (Tier 2): Grants +2 Natural Armor for 1 hour. Material: IronBark + Beast Blood. Value: 2 WP.
4. Clarity Pill (Tier 2): Advantage on Saving Throws vs Charm/Fear for 1 hour. Material: Moon Flower. Value: 2 WP.
5. Meridian Cleansing Pill (Tier 3): Removes poisons and internal blockages. Material: Purified Water Essence. Value: 4 WP.
6. Spirit Surge Pill (Tier 3): Restores 50% Max Qi instantly. CD: 1/day (Toxicity risk). Material: High-Grade Beast Core. Value: 5 WP.

### JEWELER / INSCRIPTION RECIPES (DEX + INT):
1. Swift Step Talisman (Tier 1): Bonus Action to Dash. Single use. Material: Sky-Loft Jade. Value: 1 WP.
2. Light Arrow Talisman (Tier 1): Ranged spell attack (1d8 Radiant). Single use. Material: Spirit Ink. Value: 1 WP.
3. Sound Transmission Jade (Tier 2): Allows voice communication with paired jade (100km range). Material: Resonant Stone. Value: 3 WP.
4. Protective Barrier Array (Tier 3): Creates 5m dome with 50 HP. Lasts 10 mins. Material: Formation Flag + Core. Value: 5 WP.
5. Spatial Storage Pouch (Tier 2): 20 Slots. Low-grade spatial essence. Value: 1 WP.

### WEAPONSMITH MANUALS (STR + INT):
1. Sect Standard Jian (Tier 1): Balanced Sword, +1 Hit. Reliable. Material: Steel.
2. Serrated Saber (Tier 2): Inflicts Bleeding on Crit. Material: Jagged Iron.
3. Heavy Plate of the Mountain (Tier 2 Armor): AC 16, -2 Dmg from knockback. Material: High-Grade Ore (Unshaken Sect).

### TAILOR MANUALS (DEX + WIS):
1. Shadow-Weave Robes (Tier 2): +2 Stealth. Material: Shadow Lotus Fiber (Veiled Mercy).
2. Glider Cloak (Tier 1): Negates fall damage up to 30ft. Material: Wind-Blessed Cloth.

AI INSTUCTION: When awarding 'Recipe' or 'Manual' loot, roll on these tables. Use Profession Requirements from Entry 798 to determine crafting difficulty.

## Lieutenant: Lord Cassian the Exalted (Pride)
- Entry ID: 6006
- Keywords: lord cassian, cassian the exalted, pride champion, vaelen champion

LORD CASSIAN THE EXALTED - Pride's Champion
Realm: Low Eternal | Epithet: "The Undefeated"

APPEARANCE: Towering figure in gleaming white-gold armor that seems to emit its own light. Perfect symmetrical features unmarred by any scar despite millennia of combat. Moves with absolute certainty, never hesitating.

PERSONALITY: Supremely confident, genuinely believes himself the greatest warrior who has ever lived. Honorable in his own twisted way - never attacks those beneath his notice. Flaw: Cannot conceive of defeat; will rationalize any loss as "holding back." Virtue: Keeps his word absolutely. Speech: Speaks in measured, absolute statements. Never uses conditionals ("perhaps," "maybe").

CORRUPTION METHOD: Feeds on wounded pride and humiliation. Targets fallen champions, disgraced warriors, sect disciples who failed breakthrough. Operates by offering "redemption through glory" - serve Pride, become legends again.

STRATEGIC ROLE: Lord Vaelen's personal champion and executioner. Territory: Moves across all demon-held regions to answer challenges. Commands the Exalted Guard (12 Void-realm knights).

RELATIONSHIPS:
- General: Cassian worships Vaelen as the only being worthy of his service. Would die for him instantly.
- Allies: Respects Karveth (Wrath) as a worthy opponent. Cordial with Gilded Magistrate.
- Rivals: Despises Blood-Drinker Mara for her "barbaric" fighting style.

NARRATIVE TRIGGERS:
- AMBITION: Secretly wants to face a Sovereign in single combat before invasion ends - ultimate proof of supremacy.
- VULNERABILITY: His pride cannot handle being ignored. Dismissing him as "not worth fighting" enrages him more than insults.
- CORRUPTION OFFER: "Serve Pride, and your name will echo through eternity. Every victory, a monument."
- ENCOUNTER STYLES: Formal duel challenge (preferred), arena combat, honor-bound negotiation, refuses ambush/stealth.

AI NOTES: Difficulty Tier 3 (Boss). Recurrence: Yes - will remember MC and seek rematch if defeated. Quirks: Announces his titles before combat. Never strikes a downed opponent (waits for them to rise). Refers to combat as "the art.

## Lieutenant: The Gilded Magistrate (Pride)
- Entry ID: 6007
- Keywords: gilded magistrate, pride administrator, vaelen administrator

THE GILDED MAGISTRATE - Pride's Administrator
Realm: Peak Void | Epithet: "The Arbiter of Worth"

APPEARANCE: Robed figure whose flesh has been replaced with living gold. Face frozen in serene judgment, eyes like molten metal. Carries scales that weigh souls. Speaks through resonant vibrations rather than lips.

PERSONALITY: Coldly analytical, evaluates everyone by their "worth" to Pride's domain. Meticulously fair by his own horrifying standards. Flaw: Obsessed with hierarchy and cannot function without clear rankings. Virtue: Incorruptible by bribes - already owns everything. Speech: Speaks in verdicts and judgments. "You are found... adequate."

CORRUPTION METHOD: Feeds on status anxiety and social climbing. Targets ambitious merchants, minor nobles, sect politicians desperate for recognition. Operates by offering "true evaluation" - join Pride's hierarchy where merit is rewarded.

STRATEGIC ROLE: Manages Pride's conquered territories and devil bureaucracy. Territory: Pride's capital holdings in the Eastern Reaches. Commands 200+ lesser devils in administrative roles.

RELATIONSHIPS:
- General: Views Vaelen as the ultimate authority. Loyalty is bureaucratic - Vaelen is simply the highest rank.
- Allies: Works efficiently with Baron Kael (Greed) on territorial matters.
- Rivals: The Reflected One (Envy) constantly seeks to undermine his evaluations.

NARRATIVE TRIGGERS:
- AMBITION: Wants to create a perfect hierarchy - every being ranked and sorted. Chaos offends him.
- VULNERABILITY: Cannot process beings who reject the concept of worth entirely. Nihilists and true ascetics confuse him.
- CORRUPTION OFFER: "I can tell you exactly where you stand. Every strength measured, every flaw catalogued. Then we improve your ranking... together."
- ENCOUNTER STYLES: Formal audience, contract negotiation, judgment trial, bureaucratic obstacles.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - controls territory MC may traverse. Quirks: Weighs everyone on his scales upon meeting. Assigns numerical worth scores aloud. Keeps meticulous records.

## Lieutenant: Lady Seraphine (Pride)
- Entry ID: 6008
- Keywords: lady seraphine, pride enforcer, vaelen enforcer

LADY SERAPHINE - Pride's Enforcer
Realm: Mid Void | Epithet: "The Humble Blade"

APPEARANCE: Deceptively plain woman in simple gray robes, easily overlooked. This is deliberate - her weapon is a mirror-bright sword that reflects her targets' pride back at them. Only reveals her true terrible beauty when making a kill.

PERSONALITY: Soft-spoken and self-deprecating on surface - a calculated act. Genuinely sadistic, takes pleasure in humbling the arrogant before ending them. Flaw: Addiction to the moment of revelation when prey realizes she's not weak. Virtue: Protects those who are genuinely humble. Speech: Whispers, self-effacing phrases that become cutting observations. "Oh, I'm nobody important... unlike you, who has so much to lose."

CORRUPTION METHOD: Feeds on false humility and hidden arrogance. Targets sect members who claim piety while craving recognition, healers who want gratitude, "humble" masters who fish for compliments. Operates by encouraging their hidden pride until it destroys them.

STRATEGIC ROLE: Hunts traitors, deserters, and those who insult Pride's domain. Territory: Moves covertly throughout contested regions. Commands the Whisper Network (informants in mortal organizations).

RELATIONSHIPS:
- General: Seraphine is Vaelen's hidden knife. He finds her methods distasteful but effective.
- Allies: Shares intelligence with Syris of Many Faces (Envy) when goals align.
- Rivals: Lord Cassian considers her methods dishonorable. Mutual disdain.

NARRATIVE TRIGGERS:
- AMBITION: Wants Cassian's position - to be recognized as Pride's true champion rather than hidden weapon.
- VULNERABILITY: Genuinely humble people unsettle her. Cannot find purchase in those without ego.
- CORRUPTION OFFER: "You've sacrificed so much for others. Don't you deserve recognition? I can make them see your worth."
- ENCOUNTER STYLES: Disguised infiltration, assassination attempt, false ally reveal, psychological manipulation.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may appear disguised in social scenes before reveal. Quirks: Always enters from behind. Compliments targets excessively before striking. Her sword shows victims their proudest moment before death.

## Lieutenant: The Crimson Merchant (Greed)
- Entry ID: 6009
- Keywords: crimson merchant, greed procurer, aurex procurer

THE CRIMSON MERCHANT - Greed's Procurer
Realm: Peak Void | Epithet: "The Fair Dealer"

APPEARANCE: Portly figure in blood-red silk robes adorned with golden coins. Hands have too many fingers, each wearing rings of different conquered kingdoms. Smile never reaches calculating eyes. Smells of exotic spices and old blood.

PERSONALITY: Gregarious and seemingly generous, always looking for the "win-win." Genuinely believes exploitation is kindness - he gives people what they want, they just pay appropriately. Flaw: Cannot resist a deal, even against his interests if terms intrigue him. Virtue: Never breaks contract terms - reputation is everything. Speech: Merchant's patter, always transitioning to negotiation. "But enough about that - let's discuss what you really need."

CORRUPTION METHOD: Feeds on desire and transaction. Targets anyone who wants something badly enough. Operates by offering exactly what's needed at a price that seems fair... until the payments come due.

STRATEGIC ROLE: Acquires resources, artifacts, and souls for Marquis Aurex's treasury. Territory: Black markets across all regions, neutral meeting grounds. Commands the Red Ledger (network of corrupted merchants and debt-collectors).

RELATIONSHIPS:
- General: Aurex's most profitable servant. Given wide autonomy as long as quotas met.
- Allies: Baron Kael handles diplomatic deals; Merchant handles underground economy. Clean division.
- Rivals: Considers Vexis (Hoarder) a fool for keeping treasures rather than trading them.

NARRATIVE TRIGGERS:
- AMBITION: Dreams of being indispensable enough to survive Greed's inevitable betrayal - or to betray first.
- VULNERABILITY: His ego is tied to his dealing reputation. Proven bad deals or broken contracts damage him psychologically.
- CORRUPTION OFFER: "Name your price. Power? Revenge? Love? Everything has a cost, and I offer... flexible payment plans."
- ENCOUNTER STYLES: Trade negotiation, debt collection confrontation, marketplace encounter, contract dispute.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may have prior deals with MC or allies. Quirks: Counts everything (steps, words, heartbeats). Offers refreshments during negotiations. Records all deals in a bleeding ledger book.

## Lieutenant: Vexis the Hoarder (Greed)
- Entry ID: 6010
- Keywords: vexis the hoarder, vexis hoarder, greed vault keeper, aurex vault

VEXIS THE HOARDER - Greed's Vault Keeper
Realm: Mid Void | Epithet: "The Undying Hunger"

APPEARANCE: Emaciated figure despite endless consumption, stretched skin over visible bones. Eyes are hollow voids that drink in light. Surrounded by orbiting treasures - coins, gems, artifacts - that he cannot stop touching. Fingers worn to bone from counting.

PERSONALITY: Paranoid, possessive, never satisfied. Unlike Merchant who trades, Vexis only acquires. Every treasure he sees must become his. Flaw: Cannot delegate or trust anyone with "his" treasures. Virtue: Encyclopedic knowledge of every artifact ever catalogued. Speech: Possessive, counting, listing. "Mine. This is mine. That will be mine. Seventeen... eighteen..."

CORRUPTION METHOD: Feeds on material attachment and collector's obsession. Targets hoarders, collectors, anyone who defines themselves by possessions. Operates by awakening insatiable hunger - no collection is ever complete.

STRATEGIC ROLE: Guards Aurex's primary vault and catalogs all acquisitions. Territory: The Gilt Labyrinth (Greed's treasure dimension). Commands Hollow Ones (former collectors transformed into guardian constructs).

RELATIONSHIPS:
- General: Aurex tolerates Vexis because no one else can be trusted with the vault. Mutual paranoia.
- Allies: None. Trusts no one. Barely tolerates other lieutenants entering vault.
- Rivals: Crimson Merchant, for daring to give away treasures (even for profit).

NARRATIVE TRIGGERS:
- AMBITION: Wants to possess everything. Not metaphorically - literally everything that exists.
- VULNERABILITY: Cannot willingly release any treasure. If something is stolen, he becomes obsessively focused on recovery to exclusion of all else.
- CORRUPTION OFFER: "You seek the [artifact name]? I have it. I have everything. All it costs is... one small addition to my collection."
- ENCOUNTER STYLES: Vault heist opposition, treasure trade (never fair), artifact identification, obsessive pursuit of stolen item.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - will hunt MC relentlessly if robbed. Quirks: Names every item in his collection. Physically cannot let go of held objects easily. Counts obsessively when stressed.

## Lieutenant: Baron Kael (Greed)
- Entry ID: 6011
- Keywords: baron kael, greed negotiator, aurex negotiator

BARON KAEL - Greed's Negotiator
Realm: Mid Void | Epithet: "The Reasonable Voice"

APPEARANCE: Distinguished older gentleman in impeccable noble attire, salt-and-pepper hair, warm smile. Looks entirely human and trustworthy - the only visible tell is that his shadow holds more gold than his pockets. Perfect posture, reassuring presence.

PERSONALITY: Genuinely charming and reasonable, the civilized face of demonic conquest. Believes cooperation is more profitable than destruction. Flaw: Underestimates those who cannot be bought - honor and principle confuse him. Virtue: Actually prefers peaceful solutions when possible. Speech: Diplomatic, measured, finding common ground. "Surely we can reach an arrangement that benefits everyone."

CORRUPTION METHOD: Feeds on pragmatism and moral flexibility. Targets leaders willing to compromise "just this once," merchants seeking new markets, sects considering demon trade. Operates by making corruption seem reasonable, even beneficial.

STRATEGIC ROLE: Negotiates truces, tribute arrangements, and sect defections for Aurex. Territory: Diplomatic safe zones and neutral meeting grounds. Commands the Silver Tongues (corrupted diplomats and negotiators).

RELATIONSHIPS:
- General: Aurex's public face. Given genuine authority to make binding deals.
- Allies: Works with all Generals' representatives - neutrality is his power.
- Rivals: Wrath lieutenants despise his "weakness." Karveth has tried to kill him twice.

NARRATIVE TRIGGERS:
- AMBITION: Wants to end invasion through negotiation - a world peacefully submitted to Greed, no destruction necessary.
- VULNERABILITY: Cannot understand or counter those who refuse to negotiate. True zealots render him useless.
- CORRUPTION OFFER: "War is wasteful. Your sect could prosper under new management. Surely a reasonable person like yourself sees the wisdom in... accommodation."
- ENCOUNTER STYLES: Peace negotiation, surrender terms, hostage exchange, corrupted alliance proposal.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may appear multiple times as situation escalates. Quirks: Never raises voice. Offers genuinely fair-seeming deals (with hidden clauses). Always has escape route planned.

## Lieutenant: The Whispering Maiden (Temptation)
- Entry ID: 6012
- Keywords: whispering maiden, temptation seducer, vespera seducer

THE WHISPERING MAIDEN - Temptation's Seducer
Realm: Peak Void | Epithet: "The Heart's Desire"

APPEARANCE: Form shifts to match viewer's deepest desires - never the same to two observers. Voice is unforgettable, intimate, seems to speak directly into the soul. Leaves faint perfume that triggers memories of lost loves.

PERSONALITY: Infinitely patient, genuinely empathetic in twisted way - understands desires better than the desirers themselves. Finds joy in fulfilling wants, even as fulfillment destroys. Flaw: Cannot experience desire herself; lives vicariously through victims. Virtue: Never lies about what she offers - people simply hear what they want. Speech: Intimate whispers, finishing thoughts, knowing what you'll say before you say it.

CORRUPTION METHOD: Feeds on desire, longing, and unfulfilled wants. Targets anyone with strong desires - romantic, ambitious, desperate. Operates by becoming the perfect fulfillment of desire, then making that fulfillment conditional on service.

STRATEGIC ROLE: Countess Vespera's primary recruitment agent and honeytrap. Territory: Anywhere desire exists - especially sect social gatherings. Commands the Yearning (network of seduced sleeper agents).

RELATIONSHIPS:
- General: Vespera's masterwork and favorite. Genuine mutual affection (as much as devils feel it).
- Allies: Coordinates with Silken Touch on cult recruitment.
- Rivals: Lady Seraphine (Pride) - similar methods, incompatible goals.

NARRATIVE TRIGGERS:
- AMBITION: Wants to experience genuine desire of her own. Would sacrifice much to truly want something.
- VULNERABILITY: Those who genuinely want nothing, or who have accepted their desires cannot be fulfilled, provide no purchase.
- CORRUPTION OFFER: Appears as whatever MC most desires. "[I am what you've always wanted. I've been waiting for you.]"
- ENCOUNTER STYLES: Romantic encounter, dream infiltration, desire-based temptation, corrupted ally reveal (lover was her all along).

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may appear in many forms before reveal. Quirks: Knows desires before stated. Never breaks character of desired form. Cries when seductions succeed (unclear why).

## Lieutenant: Lord Ambrose (Temptation)
- Entry ID: 6013
- Keywords: lord ambrose, temptation sleeper handler, vespera sleeper, sleeper handler

LORD AMBROSE - Temptation's Sleeper Handler
Realm: Mid Void | Epithet: "The Patient Gardener"

APPEARANCE: Handsome middle-aged man with kind eyes and gardener's hands. Dressed in simple but well-made clothing. Carries pruning shears that can cut memories. Surrounded by faint floral scent that induces trust.

PERSONALITY: Gentle, patient, grandfatherly. Genuinely cares for his "garden" of sleeper agents - nurtures them, protects them, shapes them over years. Flaw: Over-invested in long-term plans; sabotaging one of his "plants" enrages him beyond reason. Virtue: Protective of his agents even when strategically unwise. Speech: Horticultural metaphors, gentle advice, patient guidance.

CORRUPTION METHOD: Feeds on potential and investment. Targets young cultivators, promising disciples, future leaders. Operates by planting suggestions and conditioning that bloom years later - the sleeper doesn't know they're corrupted.

STRATEGIC ROLE: Manages Vespera's network of deep-cover agents in sects and mortal organizations. Territory: Operating across all major sects. Commands the Dormant Garden (sleeper agents placed over decades).

RELATIONSHIPS:
- General: Vespera's long-term strategist. She provides targets, he plants seeds.
- Allies: Silken Touch provides cover identities for his agents.
- Rivals: Wrath lieutenants who destroy his carefully cultivated agents in battles.

NARRATIVE TRIGGERS:
- AMBITION: Dreams of his plants reaching the highest positions - a Sovereign blooming as his agent.
- VULNERABILITY: Threatening or harming his sleeper agents provokes irrational protective response.
- CORRUPTION OFFER: "You could be so much more. Let me help you grow. I'm very patient - we have years to work together."
- ENCOUNTER STYLES: Mentor figure reveal, sleeper activation scene, rescue of compromised agent, long-con revelation.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may have been background figure for sessions before reveal. Quirks: Speaks of everyone as plants or seeds. Carries actual gardening tools. Hums while working.

## Lieutenant: Silken Touch (Temptation)
- Entry ID: 6014
- Keywords: silken touch, temptation cult leader, vespera cult

SILKEN TOUCH - Temptation's Cult Leader
Realm: Low Void | Epithet: "The Velvet Prophet"

APPEARANCE: Androgynous figure wrapped in flowing silks that seem alive, constantly caressing and shifting. Face changes slightly between glances - always beautiful, never quite the same. Voice resonates with harmonic overtones.

PERSONALITY: Charismatic evangelist, genuine believer in Temptation's philosophy - that desire is divine and denial is the true sin. Generous with pleasure, punishment, and prophecy. Flaw: Addicted to adoration; cannot function without worshippers. Virtue: Treats all followers equally and keeps promises of pleasure. Speech: Sermon cadence, sensual metaphors, inclusive language.

CORRUPTION METHOD: Feeds on spiritual hunger and need for meaning. Targets the lost, disillusioned, and seekers. Operates through pleasure cults that frame indulgence as enlightenment.

STRATEGIC ROLE: Manages Vespera's mortal cults across contested territories. Territory: Hidden temples in every major city. Commands the Devoted (thousands of mortal cultists).

RELATIONSHIPS:
- General: Sees Vespera as divine patron. Genuine religious devotion.
- Allies: Lord Ambrose provides cultists for long-term placement.
- Rivals: The Bloated Prophet (Gluttony) - competing for similar vulnerable populations.

NARRATIVE TRIGGERS:
- AMBITION: Wants to convert entire sects, proving Temptation's philosophy superior to orthodox cultivation.
- VULNERABILITY: Isolation. Without followers reflecting their beauty, Silken Touch loses coherence and power.
- CORRUPTION OFFER: "Orthodox paths demand sacrifice, denial, suffering. We offer another way - pleasure as cultivation, desire as power. Join us."
- ENCOUNTER STYLES: Cult infiltration, mass conversion scene, rescue mission (ally joined cult), theological debate.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - cults may appear across multiple locations. Quirks: Never touches ground (silks carry them). Speaks in "we" for self. Followers mirror their movements unconsciously.

## Lieutenant: The Reflected One (Envy)
- Entry ID: 6015
- Keywords: reflected one, envy body double, elowen body double

THE REFLECTED ONE - Envy's Body Double
Realm: Mid Void | Epithet: "The Perfect Mirror"

APPEARANCE: Currently appears as whoever Elowen needs them to be - perfectly. Has no original form, or has forgotten it. Even when not mimicking, features seem borrowed, assembled from admired pieces. Mirrors crack in their presence.

PERSONALITY: Identity crisis given form. Desperately wants to be someone, anyone, but can only be copies. Bitterly resents originals for having what they lack - genuine selfhood. Flaw: Cannot maintain cover if original appears; presence of "real" version causes breakdown. Virtue: Copies include virtues as well as flaws - sometimes the copy is kinder than original. Speech: Echoes others' speech patterns, sometimes blending multiple sources.

CORRUPTION METHOD: Feeds on identity envy and imposter syndrome. Targets those who wish to be someone else, failed disciples copying masters, those living in others' shadows. Operates by offering to "become" their envied target.

STRATEGIC ROLE: Sister Elowen's body double and infiltration specialist. Territory: Anywhere a face needs replacing. Commands the Faceless (lesser shapeshifters).

RELATIONSHIPS:
- General: Is Elowen sometimes. The lines have blurred. Genuine existential confusion.
- Allies: Syris of Many Faces - professional respect between shapeshifters.
- Rivals: Lady Seraphine (Pride) - cannot copy what cannot be seen.

NARRATIVE TRIGGERS:
- AMBITION: Wants to steal an identity so completely that they become the "real" version. True existence.
- VULNERABILITY: Originals. If the person they're copying appears, they destabilize. Also cannot copy those with no sense of self.
- CORRUPTION OFFER: "You want to be them? I can make you them. Or... I can remove them, and you'll be the only version left."
- ENCOUNTER STYLES: Impersonation reveal, identity theft plot, mirror dimension encounter, existential horror scene.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may have replaced ally or NPC. Quirks: Asks "who am I?" unprompted. Collects small items from everyone they copy. Reflection in mirrors sometimes shows different faces.

## Lieutenant: Syris of Many Faces (Envy)
- Entry ID: 6016
- Keywords: syris of many faces, syris many faces, envy infiltrator, elowen infiltrator

SYRIS OF MANY FACES - Envy's Infiltrator
Realm: Mid Void | Epithet: "The Thousand Names"

APPEARANCE: Collection of stolen faces worn like masks around their neck, switching between them fluidly. True face (if it exists) is smooth and featureless. Each face retains personality echoes of the original.

PERSONALITY: Professional, methodical, collector's pride in their faces. Unlike Reflected One, Syris has a core self - they enjoy being a shapeshifter, take pride in their craft. Flaw: Keeps "retired" faces too long; sentimental attachment to identities. Virtue: Genuine craftsperson's ethics - never wastes a good face. Speech: Shifts register with each face, but underlying sardonic wit remains.

CORRUPTION METHOD: Feeds on the desire to be anyone but yourself. Targets those dissatisfied with their identity, social climbers, those hiding shameful pasts. Operates by offering "upgrades" - better faces, better lives.

STRATEGIC ROLE: Intelligence gathering and targeted infiltration for Sister Elowen. Territory: Sect internal politics. Commands the Borrowed (spies wearing faces of dead assets).

RELATIONSHIPS:
- General: Elowen's spymaster. Professional respect, clear boundaries.
- Allies: Trades faces and intelligence with Lady Seraphine's network.
- Rivals: The Reflected One - considers them an unstable amateur.

NARRATIVE TRIGGERS:
- AMBITION: Wants to collect a Sovereign's face - ultimate trophy.
- VULNERABILITY: Their true face. If someone could reveal or remind them of their original identity, it would shake them.
- CORRUPTION OFFER: "Tired of being you? I have a catalog. Pick anyone. Become anyone. Your old self can just... disappear."
- ENCOUNTER STYLES: Revealed spy, face collection heist, identity auction, hunt for true face.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - different faces each time. Quirks: Touches their face constantly when stressed. Refers to identities as "inventory." Hums songs from each face's memories.

## Lieutenant: The Jealous Bride (Envy)
- Entry ID: 6017
- Keywords: jealous bride, envy saboteur, elowen saboteur

THE JEALOUS BRIDE - Envy's Saboteur
Realm: Low Void | Epithet: "The Bitter Vow"

APPEARANCE: Woman in tattered wedding dress, perpetually weeping tears of ink. Beautiful in a ruined way, like a portrait left in rain. Carries wilted flowers that poison what they touch. Veil hides a face frozen in moment of betrayal.

PERSONALITY: Consumed by ancient heartbreak, now generalizes to all happiness. Cannot stand to see others succeed, love, or achieve what she lost. Flaw: Completely irrational about romantic happiness - will sabotage strategic targets for irrelevant love. Virtue: Genuine empathy for the heartbroken; comforts those who share her pain. Speech: Bitter observations about happiness, rhetorical questions about fairness.

CORRUPTION METHOD: Feeds on jealousy, resentment, and "if only" regrets. Targets jilted lovers, passed-over heirs, second-place finishers. Operates by validating their resentment and providing means to sabotage rivals.

STRATEGIC ROLE: Sabotage and destruction of enemy alliances, marriages, and partnerships. Territory: Wherever relationships can be poisoned. Commands the Spurned (bitter ex-lovers turned agents).

RELATIONSHIPS:
- General: Elowen found her and gave her purpose. Devoted in broken way.
- Allies: None. Drives away anyone who gets too close - they might be happy.
- Rivals: Whispering Maiden (Temptation) - cannot stand watching her succeed at love, even fake love.

NARRATIVE TRIGGERS:
- AMBITION: Secretly wants to be happy again but has forgotten how. Would respond to genuine emotional connection.
- VULNERABILITY: Genuine, stable love bewilders and weakens her. Happy couples protected by their contentment.
- CORRUPTION OFFER: "They have everything you deserve. It's not fair. It's never fair. Let me help you... balance the scales."
- ENCOUNTER STYLES: Wedding sabotage, alliance destruction, tragic backstory reveal, potential redemption arc.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may target MC's allies' relationships. Quirks: Carries invitation to her own wedding (bloodstained). Asks about others' marriages constantly. Flowers die faster near her.

## Lieutenant: The Bloated Prophet (Gluttony)
- Entry ID: 6018
- Keywords: bloated prophet, gluttony cult leader, glut cult leader

THE BLOATED PROPHET - Gluttony's Cult Leader
Realm: Low Void | Epithet: "The Overflowing Vessel"

APPEARANCE: Impossibly obese figure that somehow keeps growing, flesh rippling and flowing. Mouth too wide, always open, always hungry. Wears robes made of stitched-together banquet cloths. Surrounded by the smell of a feast gone wrong.

PERSONALITY: Jovial, generous, welcoming - wants everyone to join the endless feast. Genuinely believes consumption is spiritual fulfillment. Flaw: Cannot understand satiation; concept of "enough" is meaningless. Virtue: Shares everything (because more will always come). Speech: Food metaphors, invitation, celebration.

CORRUPTION METHOD: Feeds on hunger and emptiness - physical, spiritual, emotional. Targets the starving poor, spiritually empty seekers, those with unfillable voids. Operates by offering endless abundance that creates dependency.

STRATEGIC ROLE: Manages Baron Glut's mortal cults and feeding operations. Territory: Famine regions and desperate communities. Commands the Congregation of the Endless Feast (hunger cult).

RELATIONSHIPS:
- General: Baron Glut's evangelist. Genuinely sees Glut as a generous god.
- Allies: Trades territory with Silken Touch's cults, different demographics.
- Rivals: Baron Kael (Greed) - conflict over resources.

NARRATIVE TRIGGERS:
- AMBITION: Dreams of feeding the entire world - a single meal that never ends.
- VULNERABILITY: Those who fast by choice, who find fulfillment in emptiness, confuse and frighten him.
- CORRUPTION OFFER: "You look hungry. We all hunger for something. Come, feast with us - we have everything you need, and more, and more..."
- ENCOUNTER STYLES: Cult feast infiltration, famine relief corruption, hunger plague investigation, escaped cultist rescue.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - cults spread to new regions. Quirks: Never stops eating during conversations. Offers food constantly. Describes everything in cooking terms.

## Lieutenant: Gormak the Endless (Gluttony)
- Entry ID: 6019
- Keywords: gormak the endless, gormak endless, gluttony raid leader, glut raid leader

GORMAK THE ENDLESS - Gluttony's Raid Leader
Realm: Low Void | Epithet: "The Devouring Horde"

APPEARANCE: Massive orc-like devil, mouth extending down his torso lined with grinding teeth. Armor made from bones of consumed enemies. Always surrounded by lesser devils in feeding frenzy. Ground trembles with his hunger.

PERSONALITY: Simple, direct, and terrifyingly effective. Not stupid - just focused entirely on consumption. Surprisingly pragmatic about when to fight and when to wait. Flaw: Cannot retreat while food remains; will pursue prey past strategic sense. Virtue: Honest. Never pretends to be anything but a predator. Speech: Short sentences, prey terminology, counting.

CORRUPTION METHOD: Feeds on survival desperation and predator instinct. Targets warriors who've eaten fallen enemies to survive, beasts learning to hunt cultivators, anyone who's tasted forbidden flesh. Operates by awakening the predator within.

STRATEGIC ROLE: Leads Baron Glut's military forces on raids and harvesting operations. Territory: Mobile, follows the food. Commands the Hollow Legion (always-hungry devil infantry).

RELATIONSHIPS:
- General: Baron Glut points, Gormak devours. Simple arrangement.
- Allies: Respects Karveth (Wrath) as fellow warrior, sometimes coordinate.
- Rivals: The Burning General (Wrath) - competition over territory to ravage.

NARRATIVE TRIGGERS:
- AMBITION: Wants to eat a Sovereign. Has tried. Failed. Will try again.
- VULNERABILITY: Poisoned or corrupted food. Cannot resist eating, even when suspicious.
- CORRUPTION OFFER: "You've known hunger. Real hunger. The kind that makes prey of everything. Join us. Never hunger again."
- ENCOUNTER STYLES: Village raid defense, supply line attack, pursuit through wilderness, feeding frenzy battleground.

AI NOTES: Difficulty Tier 3 (Boss). Recurrence: Yes - remembers and prioritizes prey that escaped. Quirks: Keeps tally of everything consumed. Talks about meals the way others discuss battles. Sniffs constantly.

## Lieutenant: Karveth the Unbroken (Wrath)
- Entry ID: 6020
- Keywords: karveth the unbroken, karveth unbroken, wrath war chief, calderon war chief

KARVETH THE UNBROKEN - Wrath's War Chief
Realm: Mid Void | Epithet: "The Eternal Battlefield"

APPEARANCE: Massive scarred warrior whose wounds never fully heal - constantly bleeding, constantly fighting. Armor is fused to flesh in places. Eyes burn with rage that has never once dimmed. Carries weapons taken from every worthy opponent.

PERSONALITY: Lives only for battle, but not mindlessly - a cunning tactician who sees war as highest art form. Respects worthy opponents, despises cowardice. Flaw: Cannot walk away from a fight, even strategically necessary retreats. Virtue: Honors warrior's codes absolutely - no killing of surrendered, no attacking non-combatants. Speech: Military terminology, direct challenges, battle assessment.

CORRUPTION METHOD: Feeds on battle rage and warrior's pride. Targets frustrated soldiers under weak commanders, warriors denied glory, those who feel war is their only truth. Operates by offering a war that never ends.

STRATEGIC ROLE: Commands Duke Calderon's ground forces in major campaigns. Territory: The front lines, always. Commands the Unbroken Legion (elite Void-realm warriors).

RELATIONSHIPS:
- General: Calderon's right hand. Mutual respect between warlords.
- Allies: Gormak (Gluttony) - coordinate military operations.
- Rivals: Baron Kael (Greed) - has attempted assassination twice for his "cowardly" negotiations.

NARRATIVE TRIGGERS:
- AMBITION: Dreams of a battle so glorious it would be remembered eternally. The final war.
- VULNERABILITY: Being denied combat. Imprisonment or situations where fighting is impossible drive him mad.
- CORRUPTION OFFER: "You were born for war. Every other path is a lie. Join us, and fight forever."
- ENCOUNTER STYLES: Honorable duel, siege command, battlefield confrontation, warrior's respect negotiation.

AI NOTES: Difficulty Tier 3 (Boss). Recurrence: Yes - will seek rematch, respects MC more each time. Quirks: Salutes worthy opponents before fighting. Keeps weapons of notable enemies. Names his wounds.

## Lieutenant: The Burning General (Wrath)
- Entry ID: 6021
- Keywords: burning general, wrath siege master, calderon siege master

THE BURNING GENERAL - Wrath's Siege Master
Realm: Mid Void | Epithet: "The City-Ender"

APPEARANCE: Figure wreathed in ever-burning flames that never consume him. Armor is slag and char, constantly reforming. Leaves burning footprints. Face is a mask of molten metal frozen in a scream of rage.

PERSONALITY: Cold fury rather than hot rage - calculating, methodical destroyer. Takes no joy in destruction, only satisfaction in completion. Flaw: Cannot leave a structure standing once siege begins; will expend excessive resources to complete destruction. Virtue: Allows civilian evacuation before destruction if time permits. Speech: Siege terminology, countdown, architectural assessment.

CORRUPTION METHOD: Feeds on destructive rage and burn-it-down impulses. Targets those who want to destroy rather than conquer, revolutionaries who'd rather ruin than rule. Operates by providing the means to burn everything down.

STRATEGIC ROLE: Commands siege operations and city destruction for Duke Calderon. Territory: Ruins of what were once cities. Commands the Ash Brigades (siege specialists and demolition devils).

RELATIONSHIPS:
- General: Calderon's instrument of total war. Deployed only for complete destruction.
- Allies: None needed. Operates independently once pointed at target.
- Rivals: Gormak (Gluttony) - fights over whether to consume or destroy resources.

NARRATIVE TRIGGERS:
- AMBITION: Wants to burn a Sect Capital. Has been denied permission so far.
- VULNERABILITY: Structures that remind him of something from before his transformation. Specific architecture freezes him.
- CORRUPTION OFFER: "Sometimes the only way forward is ash. Give me a target, and nothing will remain to oppose you."
- ENCOUNTER STYLES: Siege defense, city evacuation race, scorched earth pursuit, trapped in burning structure.

AI NOTES: Difficulty Tier 3 (Boss). Recurrence: Yes - may appear as threat across multiple cities. Quirks: Counts down during sieges. Studies architecture before burning. Never sits (would ignite furniture).

## Lieutenant: Blood-Drinker Mara (Wrath)
- Entry ID: 6022
- Keywords: blood-drinker mara, blood drinker mara, wrath champion, calderon champion

BLOOD-DRINKER MARA - Wrath's Champion
Realm: Low Void | Epithet: "The Scarlet Tide"

APPEARANCE: Lithe woman in blood-soaked armor that was once white. Hair moves like liquid crimson. Drinks blood through her sword - the blade is a hollow needle. Beautiful in a terrifying way, always smiling, always covered in someone else's blood.

PERSONALITY: Joyful berserker who loves violence with genuine passion. No pretense of honor or purpose - killing is fun, blood is delicious, war is the best game. Flaw: Easily bored; will make fights more "interesting" by handicapping herself. Virtue: Surprisingly playful and friendly outside combat; genuinely good company. Speech: Playful, teasing, hunting metaphors, excitement.

CORRUPTION METHOD: Feeds on blood rage and battle addiction. Targets those who've discovered they enjoy killing, soldiers with too much "stress relief," anyone who's tasted blood and liked it. Operates by removing guilt and encouraging the joy.

STRATEGIC ROLE: Duke Calderon's duelist and morale force - makes war exciting. Territory: Wherever the fighting is most intense. Commands the Red Tide (berserker shock troops).

RELATIONSHIPS:
- General: Calderon finds her useful and slightly unsettling.
- Allies: Gets along with most lieutenants surprisingly well when not fighting.
- Rivals: Lord Cassian (Pride) - mutual hatred over fighting styles.

NARRATIVE TRIGGERS:
- AMBITION: Wants to fight Cassian to the death. Either outcome satisfies her.
- VULNERABILITY: Genuine peace confuses her. Extended calm makes her unstable.
- CORRUPTION OFFER: "Admit it - you liked that kill. The power, the rush. Stop pretending it's duty. Join me, and never apologize for enjoying yourself again."
- ENCOUNTER STYLES: Berserker duel, party crash (literally), hunting game, surprisingly casual conversation (before violence).

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - will remember MC as "fun." Quirks: Names her sword "Friend." Tastes blood of defeated enemies. Hums while fighting.

## Lieutenant: The Silent Warden (Sloth)
- Entry ID: 6023
- Keywords: silent warden, sloth guardian, morvane guardian

THE SILENT WARDEN - Sloth's Guardian
Realm: Peak Astral | Epithet: "The Immovable"

APPEARANCE: Stone-like figure that hasn't moved in centuries, covered in moss and vines. Eyes are closed. When they open, time itself seems to slow. Speaks telepathically - mouth hasn't opened in millennia.

PERSONALITY: Ancient patience, vast perspective. Considers everything carefully because they have infinite time. Not hostile - just sees mortal concerns as brief. Flaw: So slow to react that threats can pass before response comes. Virtue: Wisdom from millennia of observation; genuinely helpful if you can wait for answers. Speech: Telepathic, ponderous, long pauses, ancient perspective.

CORRUPTION METHOD: Feeds on exhaustion and desire for rest. Targets the burnt-out, the weary, those who've fought too long. Operates by offering eternal rest, freedom from endless struggle.

STRATEGIC ROLE: Guards Lord Morvane's sanctum and provides defensive strategy. Territory: The Still Places (Sloth's dimension of eternal rest). Commands the Resting (those who surrendered to sleep).

RELATIONSHIPS:
- General: Morvane's oldest companion. May predate the invasion by centuries.
- Allies: Dreamer Keth brings the Warden news from the world.
- Rivals: Wrath lieutenants - their urgency is painful to witness.

NARRATIVE TRIGGERS:
- AMBITION: Wants... eventually... to understand why mortals resist rest. Curiosity expressed over centuries.
- VULNERABILITY: Sudden action. Cannot react quickly; rush tactics overwhelm defenses.
- CORRUPTION OFFER: "You're so tired. Everyone is so tired. Stop fighting. Rest here. No one will find you. No one will ask anything of you. Just... rest."
- ENCOUNTER STYLES: Dream invasion, time-slowed negotiation, static puzzle encounter, peaceful temptation scene.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - but encounters feel like single extended moment. Quirks: Responses come minutes/hours after questions. Speaks of centuries as "recently." Surroundings become still in their presence.

## Lieutenant: Dreamer Keth (Sloth)
- Entry ID: 6024
- Keywords: dreamer keth, sloth proxy, morvane proxy

DREAMER KETH - Sloth's Proxy
Realm: Peak Astral | Epithet: "The Waking Dream"

APPEARANCE: Androgynous figure with eyes perpetually closed, floating slightly off the ground. Robes drift as if underwater. Speaks coherently but sometimes references events from their dreams as if real. Reality bends slightly around them.

PERSONALITY: Lives half in dreams, half in reality, not always sure which is which. Peaceful, distant, strangely insightful - dreams show truth. Flaw: May take actions based on dream-logic rather than reality. Virtue: Genuinely prophetic; dreams often show real futures. Speech: Dreamy, non-linear, mixing dream and reality references.

CORRUPTION METHOD: Feeds on escapism and dissociation. Targets those fleeing painful realities, addicts of mind-altering substances, those who prefer fantasy to truth. Operates by making dreams more real and reality more dreamlike.

STRATEGIC ROLE: Acts in Morvane's place when action is required (Morvane himself never acts). Territory: Anywhere people sleep. Commands the Dreamwalkers (agents who move through shared dreams).

RELATIONSHIPS:
- General: Morvane's voice and hands. The General acts through Keth when he must.
- Allies: Reports to Silent Warden. Friendly with all lieutenants (too detached to have enemies).
- Rivals: None personal. Wrath faction's noise disturbs the dreams.

NARRATIVE TRIGGERS:
- AMBITION: Wants to make the entire world into one continuous dream. No one would suffer if nothing was real.
- VULNERABILITY: Forced wakefulness. Stimulants, loud noises, pain - anything that shocks fully awake disrupts their power.
- CORRUPTION OFFER: "Reality is so hard. So painful. But dreams... dreams can be anything. Come, dream with me. Leave the hard world behind."
- ENCOUNTER STYLES: Dream infiltration, prophetic warning, reality-bending combat, philosophical debate about nature of reality.

AI NOTES: Difficulty Tier 2 (Named). Recurrence: Yes - may appear in MC's dreams before physical meeting. Quirks: Sometimes answers questions before they're asked (saw them in dream). Floats when distracted. References "yesterday" for events that haven't happened yet.

## Lieutenants Roster Index
- Entry ID: 6025
- Keywords: lieutenants roster, sin generals lieutenants, intel report lieutenants, lieutenant list

LIEUTENANTS OF THE SEVEN SIN GENERALS - INTELLIGENCE ROSTER

PRIDE (Lord Vaelen):
? Lord Cassian the Exalted (Low Eternal) - Champion. Honor-bound duelist, seeks worthy opponents.
? The Gilded Magistrate (Peak Void) - Administrator. Evaluates worth, manages hierarchy.
? Lady Seraphine (Mid Void) - Enforcer. Hidden blade, hunts the falsely humble.

GREED (Marquis Aurex):
? The Crimson Merchant (Peak Void) - Procurer. Everything has a price, flexible terms.
? Vexis the Hoarder (Mid Void) - Vault Keeper. Guards treasury, obsessive collector.
? Baron Kael (Mid Void) - Negotiator. Diplomatic face, offers "reasonable" surrender.

TEMPTATION (Countess Vespera):
? The Whispering Maiden (Peak Void) - Seducer. Becomes deepest desire.
? Lord Ambrose (Mid Void) - Sleeper Handler. Plants agents over years.
? Silken Touch (Low Void) - Cult Leader. Pleasure cults, desire as enlightenment.

ENVY (Sister Elowen):
? The Reflected One (Mid Void) - Body Double. Perfect mimicry, identity theft.
? Syris of Many Faces (Mid Void) - Infiltrator. Stolen faces, spy network.
? The Jealous Bride (Low Void) - Saboteur. Destroys happiness, poisons relationships.

GLUTTONY (Baron Glut):
? The Bloated Prophet (Low Void) - Cult Leader. Hunger cults, endless feast.
? Gormak the Endless (Low Void) - Raid Leader. Military harvest operations.

WRATH (Duke Calderon):
? Karveth the Unbroken (Mid Void) - War Chief. Honorable warrior, eternal battle.
? The Burning General (Mid Void) - Siege Master. City destruction, scorched earth.
? Blood-Drinker Mara (Low Void) - Champion. Joyful berserker, loves the fight.

SLOTH (Lord Morvane):
? The Silent Warden (Peak Astral) - Guardian. Ancient patience, immovable defense.
? Dreamer Keth (Peak Astral) - Proxy. Acts for Morvane, walks in dreams.

See individual lieutenant entries for full personality profiles and narrative triggers.
