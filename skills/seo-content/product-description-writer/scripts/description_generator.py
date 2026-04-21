#!/usr/bin/env python3
"""
Product Description Generator -- Generate product descriptions for multiple platforms.

Usage:
    python description_generator.py --name "ErgoMax Pro Chair" --category "furniture" --features "Lumbar support,Mesh back,Adjustable arms" --price 299.99
    python description_generator.py --name "AI Writing Assistant" --category "saas" --platform amazon --features "GPT-4 powered,50+ templates,Team collaboration"
    python description_generator.py --input product.json --platform all --output descriptions.json
"""

import argparse
import json
import sys
from datetime import datetime

PLATFORM_FORMATS = {
    "ecommerce": {
        "name": "Standard E-commerce",
        "title_limit": 80,
        "short_desc_limit": 200,
        "full_desc_limit": 3000,
    },
    "amazon": {
        "name": "Amazon Listing",
        "title_limit": 200,
        "bullet_count": 5,
        "bullet_limit": 500,
        "description_limit": 2000,
    },
    "shopify": {
        "name": "Shopify Store",
        "title_limit": 70,
        "meta_desc_limit": 160,
        "full_desc_limit": 5000,
    },
    "etsy": {
        "name": "Etsy Listing",
        "title_limit": 140,
        "description_limit": 1000,
        "tag_count": 13,
    },
}

CATEGORY_TONES = {
    "electronics": {
        "tone": "tech-savvy, capability-focused",
        "power_words": ["powerful", "seamless", "lightning-fast", "smart", "precision"],
        "benefit_angle": "what it enables you to do",
    },
    "fashion": {
        "tone": "aspirational, identity-focused",
        "power_words": ["stunning", "effortless", "versatile", "curated", "elevated"],
        "benefit_angle": "how it makes you feel and look",
    },
    "furniture": {
        "tone": "comfort-focused, lifestyle-oriented",
        "power_words": ["ergonomic", "handcrafted", "timeless", "premium", "designed"],
        "benefit_angle": "comfort and aesthetic improvement to your space",
    },
    "food": {
        "tone": "sensory, indulgent",
        "power_words": ["artisanal", "rich", "fresh", "aromatic", "handpicked"],
        "benefit_angle": "the experience and taste journey",
    },
    "beauty": {
        "tone": "transformative, confidence-building",
        "power_words": ["radiant", "nourishing", "clinical", "luxurious", "proven"],
        "benefit_angle": "visible transformation and self-care ritual",
    },
    "saas": {
        "tone": "professional, outcome-focused",
        "power_words": ["automate", "streamline", "scale", "integrate", "accelerate"],
        "benefit_angle": "time saved and business outcomes",
    },
    "health": {
        "tone": "trustworthy, science-backed",
        "power_words": ["clinically", "natural", "effective", "gentle", "restorative"],
        "benefit_angle": "health improvement and peace of mind",
    },
    "general": {
        "tone": "clear, benefit-focused",
        "power_words": ["premium", "trusted", "easy", "reliable", "innovative"],
        "benefit_angle": "practical value and quality",
    },
}


def parse_features(features_str):
    """Parse comma-separated features string into list."""
    if not features_str:
        return []
    return [f.strip() for f in features_str.split(",") if f.strip()]


def generate_fab(feature, category_info):
    """Generate Feature-Advantage-Benefit for a single feature."""
    return {
        "feature": feature,
        "advantage": f"[How '{feature}' is better than alternatives]",
        "benefit": f"[What '{feature}' means for the customer's {category_info['benefit_angle']}]",
        "emotion": f"[How '{feature}' makes the customer feel]",
    }


def generate_ecommerce(product):
    """Generate standard e-commerce description."""
    features = product.get("features", [])
    name = product.get("name", "Product")
    category = product.get("category", "general")
    cat_info = CATEGORY_TONES.get(category, CATEGORY_TONES["general"])
    price = product.get("price")

    title = f"{name} -- {features[0] if features else 'Premium Quality'}"
    if len(title) > PLATFORM_FORMATS["ecommerce"]["title_limit"]:
        title = title[: PLATFORM_FORMATS["ecommerce"]["title_limit"] - 3] + "..."

    benefits = []
    for f in features[:4]:
        fab = generate_fab(f, cat_info)
        benefits.append(
            {
                "headline": f,
                "detail": fab["benefit"],
            }
        )

    short_desc = f"{name} with {', '.join(features[:2])}. {cat_info['power_words'][0].capitalize()} design for {cat_info['benefit_angle']}."
    if len(short_desc) > PLATFORM_FORMATS["ecommerce"]["short_desc_limit"]:
        short_desc = short_desc[: PLATFORM_FORMATS["ecommerce"]["short_desc_limit"] - 3] + "..."

    return {
        "platform": "ecommerce",
        "title": title,
        "short_description": short_desc,
        "benefits": benefits,
        "specifications": [{"feature": f, "value": "[Value]"} for f in features],
        "suggested_cta": "Add to Cart",
        "price": price,
        "tone": cat_info["tone"],
        "title_chars": len(title),
        "short_desc_chars": len(short_desc),
    }


def generate_amazon(product):
    """Generate Amazon listing format."""
    features = product.get("features", [])
    name = product.get("name", "Product")
    brand = product.get("brand", "[Brand]")
    category = product.get("category", "general")
    cat_info = CATEGORY_TONES.get(category, CATEGORY_TONES["general"])

    title = f"{brand} {name} - {features[0] if features else ''} - {cat_info['power_words'][0].capitalize()} Design"
    if len(title) > PLATFORM_FORMATS["amazon"]["title_limit"]:
        title = title[: PLATFORM_FORMATS["amazon"]["title_limit"] - 3] + "..."

    bullets = []
    for i, f in enumerate(features[:4]):
        fab = generate_fab(f, cat_info)
        bullet = f"{f.upper()}: {fab['benefit']} -- {fab['advantage']}"
        bullets.append(bullet)

    bullets.append(
        "100% SATISFACTION GUARANTEE: We stand behind every product. "
        "If you're not completely satisfied, contact our support team for a full refund. "
        "Your satisfaction is our priority."
    )

    return {
        "platform": "amazon",
        "title": title,
        "bullets": bullets,
        "description_sections": {
            "brand_story": f"{brand} -- [Brand mission and story]",
            "problem": f"[Common problem that {name} solves]",
            "solution": f"[How {name} addresses the problem with {', '.join(features[:3])}]",
            "social_proof": "[Customer review highlights, awards, certifications]",
            "cta": f"Order your {name} today and [primary benefit].",
        },
        "backend_keywords": f"[keyword suggestions based on: {' '.join(features)}]",
        "title_chars": len(title),
    }


def generate_shopify(product):
    """Generate Shopify store description."""
    features = product.get("features", [])
    name = product.get("name", "Product")
    category = product.get("category", "general")
    cat_info = CATEGORY_TONES.get(category, CATEGORY_TONES["general"])
    price = product.get("price")

    meta_title = f"{name} - {features[0] if features else cat_info['power_words'][0].capitalize()}"
    if len(meta_title) > PLATFORM_FORMATS["shopify"]["title_limit"]:
        meta_title = meta_title[: PLATFORM_FORMATS["shopify"]["title_limit"] - 3] + "..."

    meta_desc = f"{name}: {cat_info['power_words'][0]} {cat_info['benefit_angle']}. {features[0] if features else ''}. Shop now with free shipping."
    if len(meta_desc) > PLATFORM_FORMATS["shopify"]["meta_desc_limit"]:
        meta_desc = meta_desc[: PLATFORM_FORMATS["shopify"]["meta_desc_limit"] - 3] + "..."

    return {
        "platform": "shopify",
        "meta_title": meta_title,
        "meta_description": meta_desc,
        "page_sections": {
            "hero_headline": f"{name} -- [Primary Benefit Statement]",
            "hero_subhead": f"[How it delivers {cat_info['benefit_angle']}]",
            "benefits": [
                {"title": f, "description": f"[Benefit explanation for {f}]"}
                for f in features[:4]
            ],
            "specifications": [{"label": f, "value": "[Value]"} for f in features],
            "trust_signals": [
                "Free shipping on orders over $50",
                "30-day money-back guarantee",
                "Secure checkout",
            ],
        },
        "suggested_url_slug": name.lower().replace(" ", "-"),
        "price": price,
        "meta_title_chars": len(meta_title),
        "meta_desc_chars": len(meta_desc),
    }


def generate_etsy(product):
    """Generate Etsy listing format."""
    features = product.get("features", [])
    name = product.get("name", "Product")
    category = product.get("category", "general")
    cat_info = CATEGORY_TONES.get(category, CATEGORY_TONES["general"])

    title = f"{name} - {' - '.join(features[:3])} - Gift Idea"
    if len(title) > PLATFORM_FORMATS["etsy"]["title_limit"]:
        title = title[: PLATFORM_FORMATS["etsy"]["title_limit"] - 3] + "..."

    tags = []
    for f in features:
        tags.append(f.lower())
    tags.extend([name.lower(), category, "gift"])
    tags = tags[: PLATFORM_FORMATS["etsy"]["tag_count"]]

    return {
        "platform": "etsy",
        "title": title,
        "description": (
            f"Welcome! Thank you for visiting our shop.\n\n"
            f"This {name.lower()} features {', '.join(features[:3]).lower()}. "
            f"[Expand with sensory details, materials, and the making process.]\n\n"
            f"DETAILS:\n"
            + "\n".join(f"- {f}: [value]" for f in features)
            + "\n\nSHIPPING:\n- [Shipping details]\n\n"
            f"CARE INSTRUCTIONS:\n- [Care details]\n\n"
            f"Thank you for supporting small business!"
        ),
        "tags": tags,
        "title_chars": len(title),
    }


GENERATORS = {
    "ecommerce": generate_ecommerce,
    "amazon": generate_amazon,
    "shopify": generate_shopify,
    "etsy": generate_etsy,
}


def generate_schema_markup(product):
    """Generate Product schema markup."""
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": product.get("name", ""),
        "description": f"[Short description of {product.get('name', 'product')}]",
        "brand": {"@type": "Brand", "name": product.get("brand", "[Brand]")},
        "sku": product.get("sku", "[SKU]"),
        "offers": {
            "@type": "Offer",
            "priceCurrency": "USD",
            "price": str(product.get("price", "0")),
            "availability": "https://schema.org/InStock",
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate product descriptions for multiple platforms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --name "ErgoMax Chair" --category furniture --features "Lumbar support,Mesh back" --price 299.99
  %(prog)s --name "AI Writer" --category saas --platform amazon --features "GPT-4,50+ templates"
  %(prog)s --input product.json --platform all --output descriptions.json
        """,
    )
    parser.add_argument("--name", help="Product name")
    parser.add_argument("--brand", help="Brand name")
    parser.add_argument(
        "--category",
        choices=list(CATEGORY_TONES.keys()),
        default="general",
        help="Product category for tone matching",
    )
    parser.add_argument(
        "--features", help="Comma-separated list of product features"
    )
    parser.add_argument("--price", type=float, help="Product price")
    parser.add_argument("--sku", help="Product SKU")
    parser.add_argument(
        "--platform",
        choices=list(GENERATORS.keys()) + ["all"],
        default="ecommerce",
        help="Target platform (default: ecommerce)",
    )
    parser.add_argument("--input", help="JSON file with product data")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument(
        "--include-schema",
        action="store_true",
        help="Include Product schema markup",
    )

    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            product = json.load(f)
    else:
        product = {
            "name": args.name or "Product Name",
            "brand": args.brand or "[Brand]",
            "category": args.category,
            "features": parse_features(args.features) if args.features else ["Feature 1", "Feature 2", "Feature 3"],
            "price": args.price,
            "sku": args.sku,
        }

    platforms = list(GENERATORS.keys()) if args.platform == "all" else [args.platform]

    results = {
        "generated_at": datetime.now().isoformat(),
        "product": {
            "name": product.get("name"),
            "category": product.get("category"),
            "features": product.get("features"),
        },
        "descriptions": [],
    }

    for platform in platforms:
        desc = GENERATORS[platform](product)
        results["descriptions"].append(desc)

    if args.include_schema:
        results["schema_markup"] = generate_schema_markup(product)

    output = json.dumps(results, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Descriptions written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
