import random
import os
os.system('cls')
from colorama import Fore, Back

word_list = [
    "aback", "abase", "abate", "abbey", "abbot", "abhor", "abide", "abled", "abode", "abort",
    "about", "above", "abuse", "abyss", "acorn", "acrid", "actor", "acute", "adage", "adapt",
    "adept", "admin", "admit", "adobe", "adopt", "adore", "adorn", "adult", "affix", "afire",
    "afoot", "afoul", "after", "again", "agape", "agate", "agent", "agile", "aging", "aglow",
    "agony", "agree", "ahead", "aider", "aisle", "alarm", "album", "alert", "algae", "alibi",
    "alien", "align", "alike", "alive", "allay", "alley", "allot", "allow", "alloy", "aloft",
    "alone", "along", "aloof", "aloud", "alpha", "altar", "alter", "amass", "amaze", "amber",
    "amble", "amend", "amiss", "amity", "among", "ample", "amply", "amuse", "angel", "anger",
    "angle", "angry", "angst", "anime", "ankle", "annex", "annoy", "annul", "anode", "antic",
    "anvil", "aorta", "apart", "aphid", "aping", "apnea", "apple", "apply", "apron", "aptly",
    "arbor", "ardor", "arena", "argue", "arise", "armor", "aroma", "arose", "array", "arrow",
    "arson", "artsy", "ascot", "ashen", "aside", "askew", "assay", "asset", "atoll", "atone",
    "attic", "audio", "audit", "augur", "aunty", "avail", "avert", "avian", "avoid", "await",
    "awake", "award", "aware", "awash", "awful", "awoke", "axial", "axiom", "axion", "azure",
    "bacon", "badge", "badly", "bagel", "baggy", "baker", "baler", "balmy", "banal", "banjo",
    "barge", "baron", "basal", "basic", "basil", "basin", "basis", "baste", "batch", "bathe",
    "baton", "batty", "bawdy", "bayou", "beach", "beady", "beard", "beast", "beech", "beefy",
    "befit", "began", "begat", "beget", "begin", "begun", "being", "belch", "belie", "belle",
    "belly", "below", "bench", "beret", "berry", "berth", "beset", "betel", "bevel", "bezel",
    "bible", "bicep", "biddy", "bigot", "bilge", "billy", "binge", "bingo", "biome", "birch",
    "birth", "bison", "bitty", "black", "blade", "blame", "bland", "blank", "blare", "blast",
    "blaze", "bleak", "bleat", "bleed", "bleep", "blend", "bless", "blimp", "blind", "blink",
    "bliss", "blitz", "bloat", "block", "bloke", "blond", "blood", "bloom", "blown", "bluer",
    "bluff", "blunt", "blurb", "blurt", "blush", "board", "boast", "bobby", "boney", "bongo",
    "bonus", "boost", "booth", "boozy", "borax", "borne", "bossy", "botch", "bough", "boule",
    "bound", "bowel", "boxer", "brace", "braid", "brain", "brake", "brand", "brash", "brass",
    "brave", "bravo", "brawl", "brawn", "bread", "break", "breed", "briar", "bribe", "brick",
    "bride", "brief", "brine", "bring", "brink", "briny", "brisk", "broad", "broil", "broke",
    "brood", "brook", "broom", "broth", "brown", "brunt", "brush", "brute", "buddy", "budge",
    "buggy", "bugle", "build", "built", "bulky", "bully", "bunch", "bunny", "burly", "burnt",
    "burst", "bused", "bushy", "butch", "butte", "buxom", "buyer", "bylaw", "boons", "beaky", 
    "cabal", "cabby",
    "cabin", "cable", "cacao", "cache", "cacti", "caddy", "cadet", "cagey", "cairn", "camel",
    "cameo", "canal", "candy", "canny", "canoe", "canon", "caper", "caput", "carat", "cargo",
    "carol", "carry", "carve", "caste", "catch", "cater", "catty", "caulk", "cause", "cavil",
    "cease", "cedar", "cello", "chafe", "chaff", "chain", "chair", "chalk", "champ", "chant",
    "chaos", "chard", "charm", "chart", "chase", "chasm", "cheap", "cheat", "check", "cheek",
    "cheer", "chess", "chest", "chick", "chide", "chief", "child", "chili", "chill", "chime",
    "china", "chirp", "chock", "choir", "choke", "chord", "chore", "chose", "chuck", "chump",
    "chunk", "churn", "chute", "cider", "cigar", "cinch", "circa", "civic", "civil", "clack",
    "claim", "clamp", "clang", "clank", "clash", "clasp", "class", "clean", "clear", "cleat",
    "cleft", "clerk", "click", "cliff", "climb", "cling", "clink", "cloak", "clock", "clone",
    "close", "cloth", "cloud", "clout", "clove", "clown", "cluck", "clued", "clump", "clung",
    "coach", "coast", "cobra", "cocoa", "colon", "color", "comet", "comfy", "comic", "comma",
    "conch", "condo", "conic", "copse", "coral", "corer", "corny", "corps", "couch", "cough", 
    "could", "count", "coupe", "court", "coven", "cover", "covet", "cower", "coyly", "crack", 
    "craft", "cramp", "crane", "crank", "crash", "crass", "crate", "crave", "crawl", "craze", 
    "crazy", "creak", "cream", "credo", "creed", "creek", "creep", "creme", "crepe", "crest", 
    "crick", "cried", "crier", "crime", "crimp", "crisp", "croak", "crock", "crone", "crony", 
    "crook", "cross", "croup", "crowd", "crown", "crude", "cruel", "crumb", "crush", "crust", 
    "crypt", "cubic", "cumin", "curio", "curly", "curry", "curse", "curve", "curvy", "cutie", 
    "cyber", "cycle", "cynic", "daddy", "daily", "dairy", "daisy", "dance", "dandy", "datum", 
    "daunt", "dealt", "death", "debar", "debit", "debug", "debut", "decal", "decay", "decor", 
    "decoy", "decry", "defer", "deign", "deity", "delay", "delta", "delve", "demon", "demur", 
    "denim", "dense", "depot", "depth", "derby", "deter", "detox", "deuce", "devil", "diary", 
    "dicey", "digit", "dilly", "dimly", "diner", "dingy", "diode", "dirge", "dirty", "disco", 
    "ditch", "ditto", "ditty", "diver", "dizzy", "dodge", "dodgy", "dogma", "doing", "dolce", 
    "dolly", "donor", "donut", "dopey", "doubt", "dough", "douse", "dowdy", "dowel", "downy", 
    "dowry", "dozen", "draft", "drain", "drake", "drama", "drank", "drape", "drawl", "drawn", 
    "dread", "dream", "dress", "dried", "drier", "drift", "drill", "drink", "drive", "droit", 
    "droll", "drone", "drool", "droop", "dross", "drove", "drown", "druid", "drunk", "dryer", 
    "dryly", "duchy", "dully", "dummy", "dumpy", "dunce", "dusky", "dusty", "dutch", "duvet", 
    "dwarf", "dwell", "dwelt", "dying", "deals", "eager", "eagle", "early", "earth", "easel", 
    "eaten", 
    "eater", "ebony", "eclat", "edict", "edify", "eerie", "egret", "eight", "eject", "eking", 
    "elate", "elbow", "elder", "elect", "elegy", "elfin", "elide", "elite", "elope", "elude", 
    "email", "embed", "ember", "emcee", "empty", "enact", "endow", "enema", "enemy", "enjoy", 
    "ennui", "ensue", "enter", "entry", "envoy", "epoch", "epoxy", "equal", "equip", "erase", 
    "erect", "erode", "error", "erupt", "essay", "ester", "ether", "ethic", "ethos", "ethyl", 
    "evade", "event", "every", "evict", "evoke", "exact", "exalt", "excel", "exert", "exile", 
    "exist", "expel", "extol", "extra", "exult", "eying", "fable", "facet", "faint", "fairy", 
    "faith", "false", "fancy", "fanny", "farce", "fatal", "fatty", "fault", "fauna", "favor", 
    "feast", "fecal", "feign", "fella", "felon", "femme", "femur", "fence", "feral", "ferry", 
    "fetus", "fever", "fewer", "fiber", "ficus", "field", "fiend", "fiery", "fifth", "fifty", 
    "fight", "filer", "filet", "filly", "filmy", "filth", "final", "finch", "finer", "first", 
    "fishy", "fixer", "fizzy", "fjord", "flack", "flail", "flair", "flake", "flaky", "flame", 
    "flank", "flare", "flash", "flask", "fleck", "fleet", "flesh", "flick", "flier", "fling", 
    "flint", "flirt", "float", "flock", "flood", "floor", "flora", "floss", "flour", "flout", 
    "flown", "fluff", "fluid", "fluke", "flume", "flung", "flush", "flute", "flyer", "foamy", 
    "focal", "focus", "foggy", "foist", "folio", "folly", "foray", "force", "forge", "forgo", 
    "forte", "forth", "forty", "forum", "found", "foyer", "frail", "frame", "frank", "fraud", 
    "freak", "freed", "freer", "fresh", "friar", "fried", "frill", "frisk", "fritz", "frock", 
    "frond", "front", "frost", "froth", "frown", "froze", "fruit", "fudge", "fuels", "fugue", 
    "fully", "fungi", "funky", "funny", "furor", "furry", "fussy", "fuzzy", "fears", "gaffe", 
    "gaily", 
    "gamer", "gamma", "gamut", "gassy", "gaudy", "gauge", "gaunt", "gauze", "gavel", "gawky", 
    "gayer", "gayly", "gazer", "gecko", "geeky", "geese", "genie", "genre", "ghost", "ghoul", 
    "giant", "giddy", "gipsy", "girly", "girth", "given", "giver", "glade", "gland", "glare", 
    "glass", "glaze", "gleam", "glean", "glide", "glint", "gloat", "globe", "gloom", "glory", 
    "gloss", "glove", "glyph", "gnash", "gnome", "godly", "going", "golem", "golly", "goner", 
    "goody", "gooey", "goofy", "goose", "gorge", "gouge", "gourd", "grace", "grade", "graft", 
    "grail", "grain", "grand", "grant", "grape", "graph", "grasp", "grass", "grate", "grave", 
    "gravy", "graze", "great", "greed", "green", "greet", "grief", "grill", "grime", "grimy", 
    "grind", "gripe", "groan", "groin", "groom", "grope", "gross", "group", "grout", "grove", 
    "growl", "grown", "gruel", "gruff", "grunt", "guano", "guard", "guava", "guess", "guest", 
    "guide", "guild", "guile", "guilt", "guise", "gulch", "gully", "gumbo", "gummy", "guppy",
    "gusto", "gusty", "gypsy", "habit", "hairy", "halve", "handy", "happy", "hardy", "harem", 
    "harpy", "harry", "harsh", "haste", "hasty", "hatch", "hater", "haunt", "haute", "haven", 
    "havoc", "hazel", "heady", "heard", "heart", "heath", "heave", "heavy", "hedge", "hefty", 
    "heist", "helix", "hello", "hence", "heron", "hilly", "hinge", "hippo", "hippy", "hitch", 
    "hoard", "hoary", "hobby", "hoist", "holly", "homer", "honey", "honor", "horde", "horny", 
    "horse", "hotel", "hotly", "hound", "house", "hovel", "hover", "howdy", "human", "humid", 
    "humor", "humph", "humus", "hunch", "hunky", "hurry", "husky", "hussy", "hydro", "hyena", 
    "hymen", "hyper", "heels", "heals", "homes", "icily", "icing", "ideal", "idiom", "idiot", 
    "idler", "idyll", "igloo", 
    "iliac", "image", "imbue", "impel", "imply", "inane", "inbox", "incur", "index", "inept", 
    "inert", "infer", "ingot", "inlay", "inlet", "inner", "input", "inter", "intro", "ionic", 
    "irate", "irked", "irony", "islet", "issue", "itchy", "ivory", "jaded", "japan", "jaunt", 
    "jazzy", "jelly", "jerky", "jetty", "jewel", "jiffy", "joint", "joist", "joker", "jolly", 
    "joust", "judge", "juice", "juicy", "jumbo", "jumpy", "junta", "junto", "juror", "kappa", 
    "karma", "kayak", "kebab", "khaki", "kinky", "kiosk", "kitty", "knack", "knave", "knead", 
    "kneed", "kneel", "knelt", "knife", "knock", "knoll", "knout", "known", "koala", "krill", 
    "label", "labor", "lacey", "laden", "ladle", "lager", "lance", "lanky", "lapel", "lapse", 
    "large", "larva", "lasso", "latch", "later", "lathe", "latte", "laugh", "layer", "leach", 
    "leafy", "leaky", "leant", "leapt", "learn", "lease", "leash", "least", "leave", "ledge", 
    "leech", "leery", "lefty", "legal", "leggy", "lemon", "lemur", "leper", "level", "lever", 
    "libel", "liege", "light", "liken", "lilac", "limbo", "limit", "linen", "liner", "lingo", 
    "lipid", "lithe", "liver", "livid", "llama", "loamy", "loath", "lobby", "local", "locus", 
    "lodge", "lofty", "logic", "login", "loopy", "loose", "lorry", "loser", "louse", "lousy", 
    "lover", "lower", "lowly", "loyal", "lucid", "lucky", "lumen", "lumpy", "lunar", "lunch", 
    "lunge", "lupus", "lurch", "lurid", "lusty", "lying", "lymph", "lyric", "macaw", "macho", 
    "macro", "madam", "madly", "mafia", "magic", "magma", "maize", "major", "maker", "mambo", 
    "mamma", "mammy", "manga", "mange", "mango", "mangy", "manic", "manly", "manor", "maple", 
    "march", "marry", "marsh", "mason", "masse", "match", "matey", "matte", "mauls", "maxim", 
    "maybe", "mayor", "mealy", "meant", "meaty", "mecca", "medal", "media", "medic", "melee", 
    "melon", "mercy", "merge", "merit", "merry", "metal", "meter", "metro", "micro", "midge", 
    "midst", "might", "milky", "mimic", "mince", "miner", "minim", "minor", "minty", "minus", 
    "mirth", "miser", "missy", "mocha", "modal", "model", "modem", "mogul", "moist", "molar", 
    "money", "month", "moody", "moose", "moral", "moron", "morph", "mossy", "motel", "motif", 
    "motor", "motto", "moult", "mound", "mount", "mourn", "mouse", "mouth", "mover", "movie", 
    "mower", "mucky", "mucus", "muddy", "mulch", "mummy", "munch", "mural", "murky", "mushy", 
    "music", "musky", "musty", "myrrh", "myths", "means", "mazes", "nacho", "nadir", "naive",
    "nabob", "naked",
    "nasal", "nasty", "natal", "naval", "navel", "needy", "nerdy", "nerve", "never", "newer", 
    "newly", "nicer", "niche", "niece", "night", "ninja", "ninny", "ninth", "noble", "nobly", 
    "noise", "noisy", "nomad", "noose", "north", "nosey", "notch", "novel", "nudge", "nurse", 
    "nutty", "nylon", "oaken", "obese", "occur", "ocean", "octal", "octet", "oddly", "offal", 
    "offer", "often", "olden", "older", "olive", "ombre", "omega", "onion", "onset", "oozed", 
    "opera", "opine", "optic", "orbit", "order", "organ", "other", "otter", "ounce", "outdo", 
    "outer", "outgo", "ovary", "ovate", "overt", "ovine", "ovoid", "owing", "owner", "oxide", 
    "ozone", "paddy", "pagan", "paint", "paler", "palsy", "panel", "panic", "pansy", "papal", 
    "paper", "pappy", "parch", "parer", "parka", "parry", "parse", "party", "pasta", "paste", 
    "pasty", "patch", "patio", "patsy", "patty", "pause", "payee", "payer", "peace", "peach", 
    "pearl", "pecan", "pedal", "penal", "pence", "penne", "penny", "perch", "peril", "perky", 
    "pesky", "pesto", "petal", "peter", "petty", "phase", "phone", "phony", "photo", "piano", 
    "picky", "piece", "piety", "piggy", "pilaf", "piled", "piles", "pinky", "pinto", "pious", 
    "piper", "pique", "pitch", "pithy", "pivot", "pixel", "pixie", "pizza", "place", "plaid", 
    "plain", "plait", "plane", "plank", "plant", "plate", "plaza", "plead", "pleat", "plied", 
    "plier", "plink", "plonk", "plumb", "plume", "plump", "plunk", "plush", "poach", "poesy", 
    "point", "poise", "poker", "polar", "polka", "polyp", "pooch", "poppy", "porch", "poser", 
    "posit", "posse", "pouch", "pound", "pouty", "power", "prank", "prawn", "press", "price", 
    "prick", "pride", "pried", "prime", "primo", "print", "prior", "prise", "prism", "privy", 
    "prize", "probe", "prong", "proof", "prose", "proud", "prove", "prowl", "proxy", "prude", 
    "prune", "psalm", "psych", "pubic", "puffy", "pulpy", "pulse", "punch", "pupil", "puppy", 
    "puree", "purer", "purge", "purse", "pushy", "putty", "pygmy", "peels", "pinch", "quack", 
    "quail", "quake", 
    "qualm", "quark", "quart", "quash", "quasi", "queen", "queer", "quell", "query", "quest", 
    "quick", "quiet", "quill", "quilt", "quirk", "quite", "quota", "quote", "quoth", "rabbi", 
    "rabid", "racer", "radar", "radii", "radio", "rainy", "raise", "rajah", "rally", "ralph", 
    "ramen", "ramie", "ranch", "randy", "range", "rapid", "rarer", "raspy", "ratio", "ratty", 
    "raven", "rayon", "razor", "reach", "react", "ready", "realm", "rebar", "rebel", "rebus", 
    "rebut", "recap", "recon", "recto", "recur", "redid", "reedy", "refer", "refit", "regal", 
    "rehab", "reign", "relax", "relay", "relic", "remit", "renal", "renew", "repay", "reply", 
    "reset", "resin", "retch", "retro", "retry", "reuse", "revel", "revue", "rhino", "rhyme", 
    "rider", "ridge", "rifle", "right", "rigid", "rigor", "rinse", "ripen", "riper", "risen", 
    "riser", "risky", "rival", "river", "rivet", "roach", "roast", "robin", "robot", "rocky", 
    "rodeo", "roger", "rogue", "roomy", "roost", "rosin", "rotor", "rouge", "rough", "round", 
    "rouse", "route", "rover", "rowdy", "rower", "royal", "ruddy", "ruder", "rugby", "ruler", 
    "rumba", "rumor", "rupee", "rural", "rusty", "reshi", "runny", "runty", "sadly", "safer", 
    "saint", "salad", "sally", 
    "salon", "salsa", "salty", "salve", "salvo", "sandy", "saner", "sappy", "sassy", "satin", 
    "satyr", "sauce", "saucy", "sauna", "saute", "savor", "savvy", "scald", "scale", "scalp", 
    "scaly", "scamp", "scant", "scarf", "scary", "scene", "scent", "scion", "scoff", "scold", 
    "scone", "scoop", "scope", "score", "scorn", "scour", "scout", "scowl", "scram", "scrap",
    "scrub", "scuba", "scuff", "seamy", "sedan", "seedy", "segue", "seize", "sense", "sepia", 
    "serif", "serum", "serve", "setup", "seven", "sever", "sewer", "shack", "shade", "shady", 
    "shaft", "shake", "shaky", "shale", "shall", "shame", "shank", "shape", "shard", "share", 
    "shark", "sharp", "shave", "shear", "sheen", "sheep", "sheer", "sheet", "sheik", "shelf", 
    "shell", "shift", "shine", "shiny", "shire", "shirk", "shirt", "shoal", "shock", "shone", 
    "shook", "shoot", "shore", "shorn", "short", "shout", "shove", "shown", "showy", "shrew", 
    "shrub", "shrug", "shuck", "shunt", "shush", "shyly", "sided", "siege", "sieve", "sight", 
    "sigma", "signs", "silky", "silly", "since", "sinew", "singe", "siren", "sissy", "sixth", 
    "sixty", "sized", "skate", "skier", "skiff", "skill", "skimp", "skirt", "skulk", "skull", 
    "skunk", "slack", "slain", "slang", "slant", "slash", "slate", "slave", "sleek", "sleep", 
    "sleet", "slept", "slice", "slick", "slide", "slime", "slimy", "sling", "slink", "sloop", 
    "slope", "sloth", "slump", "slung", "slurp", "slush", "slyly", "smack", "small", "smart", 
    "smash", "smear", "smell", "smelt", "smile", "smirk", "smite", "smith", "smock", "smoke", 
    "smoky", "smote", "snack", "snail", "snake", "snaky", "snare", "snarl", "sneak", "sneer", 
    "snide", "snipe", "snoop", "snore", "snort", "snout", "snowy", "snuck", "soapy", "sober", 
    "soggy", "solar", "solid", "solve", "sonar", "sonic", "sooth", "sorry", "sound", "soupy", 
    "sower", "space", "spade", "spank", "spare", "spark", "spasm", "spawn", "speak", "spear", 
    "speck", "speed", "spell", "spend", "spent", "sperm", "spice", "spicy", "spied", "spiel", 
    "spike", "spill", "spilt", "spine", "spiny", "spire", "spite", "splat", "split", "spoil", 
    "spoke", "spoof", "spook", "spool", "spoon", "spore", "sport", "spout", "spray", "spree", 
    "sprig", "spunk", "spurn", "spurt", "squad", "squat", "squib", "stack", "staff", "stage", 
    "staid", "stain", "stair", "stake", "stale", "stalk", "stall", "stamp", "stand", "stank", 
    "stare", "stark", "start", "stash", "state", "stave", "stead", "steak", "steal", "steam", 
    "steel", "steep", "steer", "stein", "stern", "stick", "stiff", "still", "stilt", "sting", 
    "stink", "stint", "stock", "stoic", "stoke", "stole", "stomp", "stone", "stony", "stood", 
    "stool", "stoop", "store", "stork", "storm", "story", "stout", "stove", "strap", "straw", 
    "stray", "strip", "strut", "stuck", "study", "stuff", "stump", "stung", "stunk", "stunt", 
    "style", "suave", "sugar", "suing", "suite", "sulky", "sully", "sumac", "sunny", "super", 
    "surer", "surge", "surly", "sushi", "swami", "swamp", "swarm", "swash", "swath", "swear", 
    "sweat", "sweet", "swell", "swept", "swift", "swill", "swine", "swing", "swirl", "swish", 
    "swoon", "swoop", "sword", "sworn", "synod", "syrup", "seals", "seams", "stays", "tabby",
    "taboo", "tacit", "table",
    "tacky", "taffy", "taint", "taken", "taker", "tally", "talon", "tamer", "tango", "tangy", 
    "taper", "tapir", "tardy", "tarry", "taste", "tasty", "tatty", "taunt", "tawny", "teach", 
    "tease", "teddy", "teeth", "tempo", "tenet", "tenor", "tense", "tenth", "tepee", "tepid", 
    "terra", "terse", "testy", "thank", "theft", "their", "theme", "there", "these", "theta", 
    "thick", "thief", "thigh", "thing", "think", "third", "thorn", "those", "three", "threw", 
    "throb", "throw", "thrum", "thumb", "thump", "thyme", "tiara", "tibia", "tidal", "tiger", 
    "tight", "tilde", "timer", "timid", "tinge", "tipsy", "titan", "tithe", "title", "toast", 
    "today", "toddy", "token", "tonal", "tonga", "tonic", "tooth", "topaz", "topic", "torch", 
    "torso", "total", "totem", "touch", "tough", "towel", "tower", "toxic", "toxin", "trace", 
    "track", "tract", "trade", "trail", "train", "trait", "tramp", "trash", "trawl", "tread", 
    "treat", "trend", "triad", "trial", "tribe", "trick", "tried", "tripe", "trite", "troll", 
    "troop", "trope", "trout", "trove", "truce", "truck", "truer", "truly", "trump", "trunk", 
    "truss", "trust", "truth", "tulip", "tummy", "tumor", "tuned", "tuner", "tunic", "turbo",
    "turfy", "turns", "tutor", "twang", "tweak", "tweed", "tweet", "twice", "twine", "twirl", 
    "twist", "twixt", "tying", "udder", "ulcer", "ultra", "uncle", "uncut", "under", "undid", 
    "undue", "unfed", "unfit", "unify", "union", "unite", "unity", "unlit", "unmet", "unset", 
    "untie", "until", "unwed", "unzip", "upper", "upset", "urban", "urged", "urine", "usage", 
    "usher", "using", "usual", "usurp", "utile", "utter", "vague", "valet", "valid", "valor", 
    "value", "valve", "vapor", "vault", "vaunt", "vegan", "vegas", "venom", "venue", "verge", 
    "verse", "verso", "vests", "vexed", "vicar", "vices", "video", "vigil", "vigor", "villa", 
    "vinyl", "viola", "viper", "viral", "virus", "visit", "vital", "vivid", "vixen", "vocal", 
    "vodka", "vogue", "voice", "voila", "vomit", "voted", "voter", "votes", "vouch", "vowel", 
    "vowed", "vowel", "vying", "wacky", "wafer", "wager", "wagon", "waist", "waive", "waltz", 
    "warty", "waste", "watch", "water", "waver", "waxen", "weary", "weave", "wedge", "weedy", 
    "weigh", "weird", "welch", "welsh", "whack", "whale", "wharf", "wheat", "wheel", "where", 
    "which", "whiff", "while", "whine", "whiny", "whirl", "whisk", "white", "whole", "whoop", 
    "whose", "widen", "wider", "widow", "width", "wield", "wight", "wilds", "wimpy", "wince", 
    "winch", "winds", "windy", "wined", "wines", "wings", "winks", "wiped", "wipes", "wires", 
    "wired", "wiser", "wisps", "wispy", "witch", "witty", "wives", "woman", "women", 
    "wonky", "woods", "woody", "wooed", "wooer", "wooly", "woozy", "words", "wordy", "works", 
    "world", "worms", "worry", "worse", "worst", "worth", "would", "wound", "woven", "wrack", 
    "wrath", "wreak", "wreck", "wrest", "wring", "wrist", "write", "wrong", "wrote", "wrung", 
    "wryly", "yacht", "yahoo", "yanks", "yards", "yarns", "yearn", "years", "yeast", "yield", 
    "young", "yours", "youth", "yummy", "zebra", "zeros", "zesty", "zonal", "zones", "zooey"
]
name_list = [
    "aidan", "clara", "caleb", "drake", "eliza", "frank", "glenn", "henry", "isaac", "jason", 
    "julie", "joann", "logan", "lucia", "laney", "paige", "raine", "susan", "steve", "saria", 
    "zaria", "zelda"
    ]

# Function to provide feedback on the guess
def get_feedback(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append(Back.GREEN + Fore.BLACK + guess[i] + Back.RESET + Fore.RESET)  # Correct letter in the correct place
        elif guess[i] in secret_word:
            feedback.append(Back.YELLOW + Fore.BLACK + guess[i] + Back.RESET + Fore.RESET)  # Correct letter in the wrong place
        else:
            feedback.append(Back.RED + Fore.BLACK + guess[i] + Back.RESET + Fore.RESET)  # Incorrect letter
    return ''.join(feedback)

def read_win_streak():
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "wordle_win_streak.txt")
        with open(file_path) as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0
    
def write_win_streak(streak):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "wordle_win_streak.txt")
    with open(file_path, "w") as file:
        file.write(str(streak))

# Main game function
def play_Wordle():
    secret_word = random.choice(word_list)
    attempts = 6
    print(
        Fore.LIGHTBLUE_EX + "Welcome to Wordle! Guess the 5-letter word. " + Fore.RED + 
        "Red" + Fore.LIGHTBLUE_EX + " means wrong letter, " + Fore.YELLOW + "Yellow" + 
        Fore.LIGHTBLUE_EX + " means right letter wrong place, " + Fore.GREEN + "Green" 
        + Fore.LIGHTBLUE_EX + " means right letter right place."
        )
    wordle_win_streak = read_win_streak()
    print("your win streak is currently:", wordle_win_streak)

    while attempts > 0:
        guess = input(Fore.LIGHTBLUE_EX + "Enter your guess: "  + Fore.RESET).lower()
        if len(guess) != 5:
            print(Fore.LIGHTBLUE_EX + "Please enter a 5-letter word.")
            continue
        if guess in name_list:
            print(Fore.LIGHTBLUE_EX + "Names cannot be used. Try again.")
            continue
        if guess not in word_list:
            print(Fore.LIGHTBLUE_EX + "Word does not exist. Try again.")
            continue

        feedback = get_feedback(secret_word, guess)
        print(f"Feedback: {feedback}")
        if guess == secret_word:
            print(Fore.LIGHTBLUE_EX + "Congratulatons! You guessed the word!" + Fore.RESET)
            wordle_win_streak = wordle_win_streak + 1
            write_win_streak(wordle_win_streak)
            print(wordle_win_streak)
            break

        attempts -= 1
        print(Fore.LIGHTBLUE_EX + f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(Fore.LIGHTBLUE_EX + f"Sorry, you've run out of attempts. The word was: {secret_word}" + Fore.RESET)
        wordle_win_streak = 0
        write_win_streak(wordle_win_streak)
        print("your current win streak has been reset:", wordle_win_streak)

# Run the game
play_Wordle()