# ================= DIMENSION SCHEMA WITH EXAMPLES =================

DIMENSIONS = {
    "effort_level": {
        "low": {
            "description": "Very low energy, wants quick and effortless food.",
            "examples": [
                "I am too tired to cook",
                "no energy to make food",
                "need something quick",
                "super lazy right now",
                "can't cook anything complicated",
                "just want fast food at home",
                "exhausted after classes",
                "something simple please",
                "minimum effort cooking",
                "quick snack type food",
                "don't want to spend time cooking",
                "very low energy today",
                "easy meal please",
                "lazy dinner idea",
                "fastest thing I can cook"
            ]
        },

        "medium": {
            "description": "Okay with some normal cooking effort.",
            "examples": [
                "I can cook something normal",
                "not too tired today",
                "fine with basic cooking",
                "something simple but cooked",
                "regular meal is fine",
                "I can spend some time cooking",
                "normal dinner idea",
                "nothing too fancy",
                "manageable recipe",
                "simple home food",
                "basic cooking is okay",
                "not super lazy",
                "can try a proper dish",
                "something reasonable to cook",
                "standard meal works"
            ]
        },

        "high": {
            "description": "Wants elaborate or creative cooking.",
            "examples": [
                "I want to cook something fancy",
                "let's make something special",
                "feel like cooking properly",
                "weekend cooking mood",
                "try a new recipe",
                "experiment in kitchen",
                "cook something elaborate",
                "full cooking energy today",
                "make a nice dish",
                "special dinner idea",
                "something impressive",
                "creative cooking mood",
                "cook like a chef today",
                "big meal preparation",
                "complex recipe is fine"
            ]
        }
    },

    "budget_level": {
        "low": {
            "description": "Very little money, needs cheapest food.",
            "examples": [
                "I am broke",
                "no money left",
                "cheap food please",
                "budget is very low",
                "need cheapest meal",
                "student budget crisis",
                "can't spend much",
                "low cost cooking",
                "minimal money food",
                "saving money on food",
                "very tight budget",
                "almost no cash",
                "need affordable meal",
                "cheap dinner idea",
                "economy cooking"
            ]
        },

        "medium": {
            "description": "Normal student spending range.",
            "examples": [
                "normal budget meal",
                "not too cheap not expensive",
                "regular food cost is fine",
                "standard student meal",
                "okay to spend a bit",
                "reasonable price food",
                "mid budget cooking",
                "average cost dinner",
                "normal grocery items",
                "balanced budget meal",
                "spend moderately",
                "typical home cooking",
                "nothing too costly",
                "manageable budget",
                "regular ingredients fine"
            ]
        },

        "high": {
            "description": "Cost is not a concern.",
            "examples": [
                "price doesn't matter",
                "can spend more on food",
                "premium ingredients are fine",
                "make something rich",
                "fancy expensive dish",
                "special occasion meal",
                "treat myself with food",
                "high budget dinner",
                "luxury cooking mood",
                "restaurant style at home",
                "buy good ingredients",
                "not worried about money",
                "celebration food",
                "gourmet cooking",
                "expensive recipe okay"
            ]
        }
    },

    "emotion_intent": {
        "comfort": {
            "description": "Needs emotional comfort and warmth from food.",
            "examples": [
                "I feel homesick",
                "want comfort food",
                "feeling low",
                "need something warm",
                "sad and hungry",
                "miss home food",
                "need emotional food",
                "something soothing",
                "bad day food",
                "feel down today",
                "want cozy meal",
                "need happiness food",
                "stress eating mood",
                "tired and emotional",
                "soft comforting dish"
            ]
        },

        "mood_lift": {
            "description": "Wants fun, tasty, uplifting food.",
            "examples": [
                "want something tasty",
                "craving something fun",
                "treat food mood",
                "excited to eat",
                "party food vibe",
                "snack for enjoyment",
                "something delicious",
                "happy food idea",
                "feel like indulging",
                "yummy dinner",
                "celebration snack",
                "fun recipe",
                "food for good mood",
                "cheat meal vibe",
                "enjoyable cooking"
            ]
        },

        "neutral": {
            "description": "Just regular eating without emotional need.",
            "examples": [
                "normal food",
                "just need to eat",
                "regular dinner",
                "simple daily meal",
                "nothing special",
                "standard lunch",
                "routine food",
                "basic eating",
                "usual meal",
                "just hungry",
                "daily cooking",
                "simple food",
                "ordinary dinner",
                "regular home meal",
                "standard food choice"
            ]
        }
    },

    "nutrition_intent": {
        "fuel": {
            "description": "Just filling energy food.",
            "examples": [
                "need something filling",
                "very hungry",
                "just want calories",
                "survival food",
                "heavy meal please",
                "stomach full food",
                "quick energy meal",
                "basic filling dish",
                "simple energy food",
                "big portion meal",
                "food for hunger",
                "just feed me",
                "very starving",
                "strong hunger",
                "need full meal"
            ]
        },

        "protein": {
            "description": "High protein or fitness focused food.",
            "examples": [
                "need protein food",
                "gym diet meal",
                "high protein dinner",
                "fitness food",
                "muscle gain meal",
                "healthy protein recipe",
                "post workout food",
                "protein rich dish",
                "diet friendly protein",
                "lean meal idea",
                "strength food",
                "bodybuilding food",
                "healthy protein snack",
                "clean protein meal",
                "nutrition focused protein"
            ]
        },

        "balanced": {
            "description": "Healthy and nutritionally balanced food.",
            "examples": [
                "healthy meal",
                "balanced diet food",
                "nutritious dinner",
                "clean eating",
                "light healthy dish",
                "good for health",
                "proper nutrition meal",
                "wholesome food",
                "diet conscious eating",
                "well balanced plate",
                "healthy home food",
                "not junk food",
                "good nutrients",
                "fresh healthy meal",
                "smart eating choice"
            ]
        }
    },

    "novelty_level": {
        "safe": {
            "description": "Wants familiar and risk-free food.",
            "examples": [
                "something simple",
                "usual food please",
                "safe option",
                "nothing experimental",
                "normal recipe",
                "familiar taste",
                "basic comfort meal",
                "no new experiments",
                "standard cooking",
                "simple trusted dish",
                "easy known recipe",
                "classic food",
                "regular favorite",
                "tried and tested",
                "predictable meal"
            ]
        },

        "variation": {
            "description": "Open to small twist or variation.",
            "examples": [
                "something slightly different",
                "new twist on usual food",
                "change from routine",
                "interesting but simple",
                "try small variation",
                "mild experiment",
                "different flavor maybe",
                "not same old food",
                "creative but easy",
                "new style simple dish",
                "mix things up a bit",
                "light experimentation",
                "variation of common dish",
                "fresh idea",
                "small change in recipe"
            ]
        },

        "experimental": {
            "description": "Wants creative or unusual food.",
            "examples": [
                "let's try something new",
                "experimental cooking",
                "unique recipe idea",
                "creative food mood",
                "unusual dish",
                "fusion cooking",
                "invent something",
                "bold flavors",
                "kitchen experiment",
                "completely different meal",
                "surprise me with food",
                "new cuisine",
                "innovative recipe",
                "fun cooking challenge",
                "crazy food idea"
            ]
        }
    }
}
