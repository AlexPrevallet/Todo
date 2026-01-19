#!/usr/bin/env python3
"""
eNavvi Content Generation System
Generates branded social media content and image prompts for marketing campaigns
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Optional
import argparse


class eNavviContentGenerator:
    """Main content generation engine for eNavvi marketing materials"""

    def __init__(self, config_path: str = "enavvi_brand_config.json"):
        """Initialize generator with brand configuration"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.brand_name = self.config['brand_name']
        self.value_props = self.config['value_propositions']
        self.messaging_pillars = self.config['key_messaging_pillars']

    def generate_linkedin_post(self,
                               context: str,
                               target_audience: str = "primary",
                               include_statistics: bool = True,
                               custom_hook: Optional[str] = None) -> Dict[str, str]:
        """
        Generate a LinkedIn post following eNavvi brand guidelines

        Args:
            context: Topic or focus of the post
            target_audience: primary (clinicians), secondary (patients), tertiary (pharmacists)
            include_statistics: Whether to include statistical hooks
            custom_hook: Optional custom opening hook

        Returns:
            Dictionary with post content, hashtags, and image prompt
        """

        # Select appropriate hooks based on context
        hooks = self._get_hooks(context, include_statistics)
        hook = custom_hook if custom_hook else random.choice(hooks)

        # Generate body content
        body = self._generate_body(context, target_audience)

        # Create call-to-action
        cta = self._generate_cta(context)

        # Select hashtags
        hashtags = self._select_hashtags(context, platform="linkedin")

        # Combine into full post
        post_text = f"{hook}\n\n{body}\n\n{cta}\n\n{hashtags}"

        # Generate image prompt
        image_prompt = self._generate_image_prompt(context, platform="linkedin")

        return {
            "post_text": post_text,
            "hook": hook,
            "body": body,
            "cta": cta,
            "hashtags": hashtags,
            "image_prompt": image_prompt,
            "character_count": len(post_text),
            "word_count": len(post_text.split()),
            "context": context,
            "generated_at": datetime.now().isoformat()
        }

    def _get_hooks(self, context: str, include_statistics: bool = True) -> List[str]:
        """Generate contextual hooks based on topic"""

        hooks_database = {
            "glp-1": [
                "**73% of clinics** report GLP-1 medication shortages affecting patient care. There's a better path forward.",
                "When your patient needs semaglutide today, but the supply chain says 'maybe next month'—what do you prescribe?",
                "GLP-1 shortages shouldn't mean treatment delays. Here's what forward-thinking clinicians are doing differently."
            ],
            "semaglutide": [
                "Compound semaglutide is helping clinicians maintain continuity of care during ongoing shortages.",
                "**$1,200+/month** for brand semaglutide vs. accessible compound alternatives. The math matters for patient adherence.",
                "Your patients are asking about semaglutide. Are you prepared with cost-effective, quality-assured options?"
            ],
            "tirzepatide": [
                "Tirzepatide demand has outpaced supply. Compound options are bridging the gap for patient care.",
                "When innovation meets access: how compound tirzepatide is supporting treatment continuity.",
                "**Mounjaro® shortages** are impacting practices nationwide. Here's what you need to know about alternatives."
            ],
            "drug_pricing": [
                "**86% of patients** cite cost as a barrier to medication adherence. Transparency changes that conversation.",
                "What if your patients knew the real cost before leaving your office? Prescribing would look different.",
                "Price opacity in pharmaceuticals isn't just frustrating—it's a clinical barrier to adherence."
            ],
            "compounding": [
                "Personalized medicine isn't new. But accessible, quality-assured compound prescribing? That's changing.",
                "When FDA-approved options don't fit your patient's needs, compound pharmacy becomes clinical necessity.",
                "**1 in 4 prescriptions** could benefit from compound customization. Are you leveraging this tool?"
            ],
            "drug_shortage": [
                "**300+ medications** are currently in shortage. Your prescribing platform should be part of the solution.",
                "Drug shortages are the new normal. Clinical agility requires new tools.",
                "When supply chains fail, your patients still need treatment. Here's how to maintain care continuity."
            ]
        }

        # Match context to hook category
        context_lower = context.lower()
        for key in hooks_database:
            if key in context_lower:
                return hooks_database[key]

        # Default hooks if no specific match
        return [
            "Prescribing shouldn't be complicated. But getting patients affordable, quality medications? That's been the challenge.",
            "What if prescribing came with price transparency, quality assurance, and zero platform fees?",
            "Modern prescribing requires modern tools. Here's what's changing in digital healthcare."
        ]

    def _generate_body(self, context: str, target_audience: str) -> str:
        """Generate the main body content"""

        # This is a template system - in production, you'd have more sophisticated content generation
        body_templates = {
            "glp-1": """The ongoing GLP-1 shortage has created real challenges for clinicians managing obesity and metabolic health. While brand medications face supply constraints, quality-assured compound alternatives are available through verified pharmacy networks.

Key considerations:
• **Compound semaglutide** follows the same molecular structure as brand versions
• Dosing protocols align with published clinical guidelines
• Cost transparency helps patients maintain treatment adherence
• Access through platforms that integrate with existing e-prescribing workflows

Treatment continuity shouldn't depend on supply chain luck. eNavvi connects clinicians to quality-assured compound pharmacy partners with real-time pricing transparency—at no cost to your practice.""",

            "semaglutide": """Semaglutide has transformed metabolic health management, but access challenges persist. For clinicians, compound semaglutide offers a clinically sound alternative during shortages or when cost barriers affect adherence.

What you need to know:
• **FDA allows compounding** during drug shortages (Sections 503A/503B)
• Standard dosing: 0.25mg weekly, titrated to therapeutic levels
• Cost comparison: Brand $1,200+/month vs compound options at significantly lower price points
• Quality assurance through USP <795> and <797> compliant pharmacies

eNavvi provides direct access to vetted compound pharmacy networks with transparent pricing—helping you prescribe with confidence, cost-effectively.""",

            "drug_pricing": """Prescription drug pricing opacity is more than frustrating—it's a clinical barrier. When patients abandon prescriptions due to unexpected costs, therapeutic plans fail.

The transparency advantage:
• **Real-time pricing** at the point of prescribing
• Compare brand vs. generic vs. compound options instantly
• No insurance authorization delays for compound medications
• Direct pharmacy shipping improves adherence

eNavvi brings pricing visibility into your prescribing workflow, empowering better conversations and outcomes with patients.""",

            "compounding": """Compound pharmacy is essential medicine—not alternative medicine. When commercial medications don't meet specific patient needs, compounding provides clinical flexibility.

Clinical applications:
• **Customized dosing** for pediatric or geriatric patients
• Alternative delivery methods (topical, sublingual, troches)
• Allergen-free formulations
• Discontinued medication recreation
• Combination therapies optimized for adherence

eNavvi connects prescribers to quality-assured compound pharmacies with clinical dosing support and transparent pricing—expanding your therapeutic toolkit at no cost to your practice."""
        }

        # Match context and return appropriate body
        context_lower = context.lower()
        for key in body_templates:
            if key in context_lower:
                return body_templates[key]

        # Default body
        return f"""eNavvi is transforming how clinicians prescribe by providing transparency, quality assurance, and cost-effective options for patients.

Our platform offers:
• **Zero fees** for prescribers—completely free to use
• Real-time pricing for brand, generic, and compound medications
• Quality-assured pharmacy network with verified compliance
• Seamless e-prescribing integration
• Clinical support and dosing protocols

{context}

Join the growing network of clinicians who are prescribing smarter, not harder."""

    def _generate_cta(self, context: str) -> str:
        """Generate appropriate call-to-action"""

        ctas = [
            "Learn more about prescriber-friendly compound solutions at eNavvi.com",
            "Curious about transparent pricing for your practice? Visit eNavvi.com",
            "Explore quality-assured compound options at eNavvi.com—free for prescribers",
            "Ready to prescribe with price transparency? Connect at eNavvi.com",
            "Discover how eNavvi is supporting clinicians at eNavvi.com"
        ]

        return random.choice(ctas)

    def _select_hashtags(self, context: str, platform: str = "linkedin", count: int = 5) -> str:
        """Select appropriate hashtags based on context and platform"""

        available_tags = self.config['common_hashtags'].get(platform, [])

        # Context-specific tags
        context_tags = {
            "glp-1": ["#WeightManagement", "#Obesity", "#MetabolicHealth"],
            "semaglutide": ["#Semaglutide", "#WeightLoss", "#GLP1"],
            "tirzepatide": ["#Tirzepatide", "#DiabetesCare"],
            "compounding": ["#CompoundPharmacy", "#PersonalizedMedicine"],
            "pricing": ["#DrugPricing", "#HealthcareAccess", "#ValueBasedCare"]
        }

        # Combine general and context-specific tags
        tag_pool = available_tags.copy()
        context_lower = context.lower()
        for key, tags in context_tags.items():
            if key in context_lower:
                tag_pool.extend(tags)

        # Select unique tags
        selected = list(set(tag_pool))[:count]
        return " ".join(selected)

    def _generate_image_prompt(self, context: str, platform: str = "linkedin") -> str:
        """Generate detailed image generation prompt for AI image tools"""

        # Base visual style for eNavvi brand
        base_style = "Professional healthcare photography, clean and modern aesthetic, medical blue and white color palette with teal accents, high-quality lighting, trustworthy and approachable mood"

        # Context-specific image prompts
        image_prompts = {
            "glp-1": f"Healthcare provider consulting with patient about weight management treatment options, modern clinic setting, digital tablet showing prescription interface, warm and professional atmosphere. {base_style}. Suitable for LinkedIn professional post.",

            "semaglutide": f"Close-up of modern prescription medication vial with clean pharmaceutical labeling, clinical setting background softly blurred, emphasis on quality and safety, professional medical photography. {base_style}. Medical stock photography style.",

            "drug_pricing": f"Split-screen composition: left side showing prescription pad with dollar signs crossed out, right side showing digital pricing transparency interface with clear cost display, professional medical office environment. {base_style}. Infographic style.",

            "compounding": f"Sterile compound pharmacy lab, pharmacist in professional attire working with precision equipment, USP standards visible, emphasis on quality control and customization, clean room environment. {base_style}. Professional pharmaceutical photography.",

            "digital_health": f"Modern physician using tablet for e-prescribing, patient consultation in contemporary medical office, seamless technology integration, trust and innovation conveyed. {base_style}. Healthcare technology editorial style.",
        }

        # Match context to prompt
        context_lower = context.lower()
        for key in image_prompts:
            if key in context_lower:
                return image_prompts[key]

        # Default prompt
        return f"Professional healthcare setting showcasing modern digital prescribing platform on tablet or computer, clinician in white coat, clean and organized medical office, emphasis on technology enabling better patient care. {base_style}. Professional medical photography for {platform}."

    def generate_twitter_post(self, context: str, include_image: bool = True) -> Dict[str, str]:
        """Generate Twitter/X post (280 character limit)"""

        twitter_templates = {
            "glp-1": "GLP-1 shortages? Compound semaglutide offers quality-assured alternatives. eNavvi connects prescribers to transparent pricing + vetted pharmacies. Free for clinicians. #HealthTech #DrugShortage",

            "pricing": "What if patients knew prescription costs before leaving your office? eNavvi brings real-time pricing to prescribing—free for clinicians. #HealthcareAccess #DrugPricing",

            "compounding": "Compound pharmacy = personalized medicine. When one-size-fits-all doesn't fit, eNavvi connects you to quality-assured custom solutions. #CompoundRx #DigitalHealth"
        }

        # Select appropriate template
        context_lower = context.lower()
        for key in twitter_templates:
            if key in context_lower:
                post_text = twitter_templates[key]
                break
        else:
            post_text = f"Prescribe smarter: eNavvi offers free digital platform for clinicians with transparent drug pricing + quality pharmacy network. {context[:80]} #HealthTech #DigitalHealth"

        # Ensure under 280 characters
        if len(post_text) > 280:
            post_text = post_text[:277] + "..."

        return {
            "post_text": post_text,
            "character_count": len(post_text),
            "image_prompt": self._generate_image_prompt(context, platform="twitter") if include_image else None,
            "context": context,
            "platform": "Twitter/X"
        }

    def generate_instagram_caption(self, context: str) -> Dict[str, str]:
        """Generate Instagram caption with visual-first approach"""

        # Instagram is more visual and conversational
        caption = f"""Quality healthcare shouldn't come with surprise bills.

eNavvi is changing prescribing by bringing transparency, affordability, and choice to clinicians and patients alike.

✨ Free for prescribers
✨ Real-time pricing
✨ Quality-assured pharmacies
✨ Compound medication access

{context}

Because better prescribing starts with better tools.

Link in bio to learn more. 💙

{self._select_hashtags(context, platform='instagram', count=8)}"""

        image_prompt = f"Instagram-optimized square format (1080x1080px): {self._generate_image_prompt(context, platform='instagram')} Bright, professional, with text overlay space at top third."

        return {
            "caption": caption,
            "image_prompt": image_prompt,
            "platform": "Instagram",
            "context": context,
            "recommended_format": "1080x1080px (square) or 1080x1350px (portrait)"
        }

    def generate_image_prompts_bulk(self, contexts: List[str], style: str = "midjourney") -> List[Dict[str, str]]:
        """
        Generate multiple image prompts for different AI image generation tools

        Args:
            contexts: List of content topics
            style: "midjourney", "dalle", or "stable-diffusion"

        Returns:
            List of formatted prompts for each context
        """

        prompts = []

        for context in contexts:
            base_prompt = self._generate_image_prompt(context)

            # Format for specific tool
            if style == "midjourney":
                formatted = f"{base_prompt} --ar 16:9 --style raw --v 6 --q 2"
            elif style == "dalle":
                formatted = f"{base_prompt} Photorealistic, 4K quality, professional photography."
            elif style == "stable-diffusion":
                formatted = f"{base_prompt}, highly detailed, professional photography, 8k uhd, dslr, high quality, film grain, Fujifilm XT3"
            else:
                formatted = base_prompt

            prompts.append({
                "context": context,
                "prompt": formatted,
                "style": style,
                "recommended_size": "1792x1024px (landscape)" if "linkedin" in base_prompt.lower() else "1024x1024px (square)"
            })

        return prompts

    def generate_campaign_suite(self, context: str) -> Dict[str, any]:
        """Generate a complete multi-platform campaign suite for a single topic"""

        return {
            "campaign_context": context,
            "linkedin": self.generate_linkedin_post(context),
            "twitter": self.generate_twitter_post(context),
            "instagram": self.generate_instagram_caption(context),
            "image_prompts": self.generate_image_prompts_bulk([context], style="midjourney")[0],
            "generated_at": datetime.now().isoformat()
        }

    def export_to_file(self, content: Dict, filename: str = None):
        """Export generated content to JSON file"""

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"enavvi_content_{timestamp}.json"

        with open(filename, 'w') as f:
            json.dump(content, f, indent=2)

        print(f"✅ Content exported to: {filename}")
        return filename


def main():
    """CLI interface for content generation"""

    parser = argparse.ArgumentParser(
        description="eNavvi Content Generation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate LinkedIn post about GLP-1 shortages:
    python content_generator.py --platform linkedin --context "GLP-1 shortage solutions"

  Generate full campaign suite:
    python content_generator.py --campaign --context "compound semaglutide"

  Generate image prompts:
    python content_generator.py --images-only --context "drug pricing transparency" --style midjourney
        """
    )

    parser.add_argument('--platform', choices=['linkedin', 'twitter', 'instagram', 'all'],
                       default='linkedin', help='Social media platform')
    parser.add_argument('--context', required=True, help='Content topic or focus')
    parser.add_argument('--campaign', action='store_true', help='Generate full multi-platform campaign')
    parser.add_argument('--images-only', action='store_true', help='Generate only image prompts')
    parser.add_argument('--style', choices=['midjourney', 'dalle', 'stable-diffusion'],
                       default='midjourney', help='Image generation tool style')
    parser.add_argument('--output', help='Output filename (JSON)')
    parser.add_argument('--custom-hook', help='Custom opening hook for LinkedIn post')

    args = parser.parse_args()

    # Initialize generator
    generator = eNavviContentGenerator()

    # Generate based on arguments
    if args.campaign:
        print(f"\n🚀 Generating full campaign suite for: {args.context}\n")
        content = generator.generate_campaign_suite(args.context)

        print("=" * 80)
        print("LINKEDIN POST")
        print("=" * 80)
        print(content['linkedin']['post_text'])
        print(f"\n📊 Stats: {content['linkedin']['word_count']} words, {content['linkedin']['character_count']} characters")

        print("\n" + "=" * 80)
        print("TWITTER/X POST")
        print("=" * 80)
        print(content['twitter']['post_text'])
        print(f"\n📊 Characters: {content['twitter']['character_count']}/280")

        print("\n" + "=" * 80)
        print("INSTAGRAM CAPTION")
        print("=" * 80)
        print(content['instagram']['caption'])

        print("\n" + "=" * 80)
        print("IMAGE GENERATION PROMPT")
        print("=" * 80)
        print(content['image_prompts']['prompt'])

    elif args.images_only:
        print(f"\n🎨 Generating image prompts for: {args.context}\n")
        prompts = generator.generate_image_prompts_bulk([args.context], style=args.style)
        content = prompts[0]

        print("=" * 80)
        print(f"IMAGE PROMPT ({args.style.upper()})")
        print("=" * 80)
        print(content['prompt'])
        print(f"\n📐 Recommended size: {content['recommended_size']}")

    elif args.platform == 'linkedin':
        print(f"\n💼 Generating LinkedIn post for: {args.context}\n")
        content = generator.generate_linkedin_post(args.context, custom_hook=args.custom_hook)

        print("=" * 80)
        print("LINKEDIN POST")
        print("=" * 80)
        print(content['post_text'])
        print(f"\n📊 Stats: {content['word_count']} words, {content['character_count']} characters")

        print("\n" + "=" * 80)
        print("IMAGE GENERATION PROMPT")
        print("=" * 80)
        print(content['image_prompt'])

    elif args.platform == 'twitter':
        print(f"\n🐦 Generating Twitter/X post for: {args.context}\n")
        content = generator.generate_twitter_post(args.context)

        print("=" * 80)
        print("TWITTER/X POST")
        print("=" * 80)
        print(content['post_text'])
        print(f"\n📊 Characters: {content['character_count']}/280")

    elif args.platform == 'instagram':
        print(f"\n📸 Generating Instagram caption for: {args.context}\n")
        content = generator.generate_instagram_caption(args.context)

        print("=" * 80)
        print("INSTAGRAM CAPTION")
        print("=" * 80)
        print(content['caption'])
        print(f"\n📐 Format: {content['recommended_format']}")

    # Export to file if requested
    if args.output or args.campaign:
        filename = generator.export_to_file(content, args.output)

    print("\n✨ Content generation complete!\n")


if __name__ == "__main__":
    main()
