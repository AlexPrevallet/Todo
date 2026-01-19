# eNavvi Content Generation System

A comprehensive healthcare marketing content generation tool designed specifically for eNavvi's brand voice, messaging pillars, and professional healthcare audience.

## 📋 Overview

This system generates:
- **LinkedIn posts** with clinical credibility and professional tone
- **Twitter/X posts** optimized for 280-character format
- **Instagram captions** with visual-first approach
- **AI image generation prompts** for Midjourney, DALL-E, and Stable Diffusion
- **Multi-platform campaign suites** with consistent messaging

## 🎯 Key Features

### ✅ Brand-Aligned Content
- Professional yet approachable tone
- Evidence-based messaging
- Healthcare-specific terminology
- Patient-centric value propositions

### ✅ Multi-Platform Support
- LinkedIn (150-250 words, professional B2B)
- Twitter/X (280 characters, concise impact)
- Instagram (visual-first, community-focused)
- Customizable for Facebook and other platforms

### ✅ Image Generation Integration
- Detailed AI image prompts for all major tools
- Platform-specific size and format recommendations
- Visual style guides for brand consistency
- Text overlay templates

### ✅ Flexible Configuration
- Topic-based content templates
- Customizable hooks and CTAs
- Audience targeting (clinicians, patients, pharmacists)
- Campaign-level content generation

---

## 🚀 Quick Start

### Option 1: Web Interface (Easiest)

1. Open `web_interface.html` in your browser
2. Enter your content topic or select a preset
3. Choose platforms and image style
4. Click "Generate Content" or "Generate Full Campaign"
5. Copy generated content directly to your clipboard

**Perfect for**: Marketing teams, quick content generation, non-technical users

### Option 2: Command Line (Advanced)

```bash
# Make the script executable
chmod +x content_generator.py

# Generate LinkedIn post
python content_generator.py --platform linkedin --context "GLP-1 shortage solutions"

# Generate full campaign suite
python content_generator.py --campaign --context "compound semaglutide for weight management"

# Generate only image prompts
python content_generator.py --images-only --context "prescription drug pricing" --style midjourney

# Export to JSON file
python content_generator.py --campaign --context "tirzepatide alternatives" --output campaign_output.json
```

**Perfect for**: Automation, batch processing, integration with other tools

---

## 📚 Usage Examples

### Example 1: LinkedIn Post for GLP-1 Shortages

```bash
python content_generator.py \
  --platform linkedin \
  --context "GLP-1 shortage solutions for weight management" \
  --custom-hook "73% of clinics report GLP-1 shortages. Here's what's working."
```

**Output:**
```
LINKEDIN POST
================================================================================
73% of clinics report GLP-1 shortages. Here's what's working.

The ongoing GLP-1 shortage has created real challenges for clinicians managing
obesity and metabolic health. While brand medications face supply constraints,
quality-assured compound alternatives are available through verified pharmacy
networks.

Key considerations:
• Compound semaglutide follows the same molecular structure as brand versions
• Dosing protocols align with published clinical guidelines
• Cost transparency helps patients maintain treatment adherence
• Access through platforms that integrate with existing e-prescribing workflows

Treatment continuity shouldn't depend on supply chain luck. eNavvi connects
clinicians to quality-assured compound pharmacy partners with real-time pricing
transparency—at no cost to your practice.

Learn more at eNavvi.com

#DigitalHealth #HealthcareInnovation #CompoundPharmacy #Telemedicine
#PhysicianLeadership

📊 Stats: 142 words, 987 characters
```

### Example 2: Full Multi-Platform Campaign

```bash
python content_generator.py --campaign --context "prescription drug pricing transparency"
```

Generates:
- LinkedIn post (professional, data-driven)
- Twitter/X post (concise, impactful)
- Instagram caption (visual, community-focused)
- AI image generation prompts (Midjourney format)
- Exported JSON with all content

### Example 3: Batch Image Prompt Generation

```bash
python content_generator.py \
  --images-only \
  --context "compound pharmacy quality assurance" \
  --style dalle
```

---

## 🎨 Image Generation Workflow

### Step 1: Generate Prompts
Use the tool to create detailed, brand-aligned image prompts:

```bash
python content_generator.py --images-only --context "your_topic" --style midjourney
```

### Step 2: Create Images
Copy the prompt and paste into your preferred tool:

**Midjourney:**
```
/imagine Healthcare provider consulting with patient about weight management
treatment options, modern clinic setting, digital tablet showing prescription
interface, warm and professional atmosphere. Professional healthcare photography,
clean and modern aesthetic, medical blue and white color palette with teal
accents, high-quality lighting, trustworthy and approachable mood.
--ar 16:9 --style raw --v 6 --q 2
```

**DALL-E 3:**
Use the generated prompt directly in ChatGPT Plus or DALL-E API

**Stable Diffusion:**
Use in platforms like Stability AI, RunwayML, or local installations

### Step 3: Post-Processing
- Resize to platform specifications (see Image Specifications below)
- Add text overlays using templates in `image_prompts_library.json`
- Ensure medical blue (#0066CC) and teal (#00A9A5) brand colors
- Test on mobile devices for readability

---

## 📐 Image Specifications by Platform

| Platform | Optimal Size | Aspect Ratio | Max File Size | Format |
|----------|-------------|--------------|---------------|---------|
| **LinkedIn** | 1200x627px | 1.91:1 | 5MB | PNG/JPEG |
| **Instagram** | 1080x1080px | 1:1 | 30MB | JPEG/PNG |
| **Twitter/X** | 1200x675px | 16:9 | 5MB | PNG/JPEG |
| **Facebook** | 1200x630px | 1.91:1 | 8MB | PNG/JPEG |

---

## 🎯 Content Topics & Templates

### Pre-Configured Topics:
1. **GLP-1 Shortages** - Addresses ongoing supply chain issues
2. **Compound Semaglutide** - Weight management solutions
3. **Tirzepatide Alternatives** - Mounjaro shortage solutions
4. **Drug Pricing Transparency** - Cost visibility for patients
5. **Compound Pharmacy Quality** - USP compliance and safety
6. **Digital Prescribing** - E-prescribing workflow integration
7. **Drug Shortage Solutions** - General supply chain resilience
8. **Personalized Medicine** - Compounding customization benefits

Each topic includes:
- Context-specific hooks with statistics
- Clinical value propositions
- Professional CTAs
- Relevant hashtags
- Optimized image prompts

---

## 🔧 Configuration

### Brand Configuration (`enavvi_brand_config.json`)

Customize your content by editing:

```json
{
  "brand_voice": {
    "attributes": ["Professional yet approachable", ...],
    "tone_guidelines": ["Never oversell or use hype language", ...]
  },
  "key_messaging_pillars": [...],
  "value_propositions": [...],
  "common_hashtags": {...}
}
```

### Image Prompt Library (`image_prompts_library.json`)

Access detailed templates for:
- Platform-specific specifications
- Visual brand identity guidelines
- Detailed image prompts by topic
- Text overlay templates
- Stock photo keywords
- Best practices for each AI tool

---

## 🎓 Best Practices

### Writing for Healthcare Audiences

**DO:**
- ✅ Use clinical terminology appropriately for HCP audiences
- ✅ Back claims with data and statistics
- ✅ Focus on patient outcomes and care quality
- ✅ Maintain professional, evidence-based tone
- ✅ Include specific dosing or clinical protocols when relevant

**DON'T:**
- ❌ Oversell or use hype language
- ❌ Make unsubstantiated clinical claims
- ❌ Use patient testimonials on LinkedIn (B2B platform)
- ❌ Include excessive emojis or casual language
- ❌ Oversimplify complex medical concepts

### Image Best Practices

**DO:**
- ✅ Use professional medical photography style
- ✅ Ensure diverse representation in people
- ✅ Maintain brand color palette (medical blue, teal, white)
- ✅ Request natural, warm lighting
- ✅ Specify "professional yet approachable" mood
- ✅ Include depth of field for visual interest

**DON'T:**
- ❌ Use overly staged or cliché stock photos
- ❌ Include outdated medical equipment
- ❌ Show identifiable patient information (HIPAA)
- ❌ Use overly clinical/sterile imagery
- ❌ Include competitor branding

---

## 📊 Command Line Reference

### Full Command Options

```bash
python content_generator.py [OPTIONS]

Options:
  --platform {linkedin,twitter,instagram,all}
                        Social media platform (default: linkedin)
  --context CONTEXT     Content topic or focus (REQUIRED)
  --campaign            Generate full multi-platform campaign
  --images-only         Generate only image prompts
  --style {midjourney,dalle,stable-diffusion}
                        Image generation tool style (default: midjourney)
  --output FILENAME     Output filename for JSON export
  --custom-hook HOOK    Custom opening hook for LinkedIn post
  -h, --help           Show this help message and exit
```

### Examples:

```bash
# LinkedIn with custom hook
python content_generator.py \
  --platform linkedin \
  --context "compound pharmacy benefits" \
  --custom-hook "1 in 4 prescriptions could benefit from customization"

# Multi-platform campaign with export
python content_generator.py \
  --campaign \
  --context "drug shortage solutions" \
  --output june_campaign.json

# Twitter content only
python content_generator.py \
  --platform twitter \
  --context "transparent prescription pricing"

# DALL-E image prompts
python content_generator.py \
  --images-only \
  --context "digital prescribing platform" \
  --style dalle
```

---

## 🔄 Workflow Integration

### Weekly Content Calendar

1. **Monday**: Generate LinkedIn thought-leadership post
   ```bash
   python content_generator.py --platform linkedin --context "weekly_topic"
   ```

2. **Wednesday**: Create Twitter engagement content
   ```bash
   python content_generator.py --platform twitter --context "mid_week_topic"
   ```

3. **Friday**: Instagram community post
   ```bash
   python content_generator.py --platform instagram --context "community_topic"
   ```

### Campaign Launch Process

1. **Generate content suite**
   ```bash
   python content_generator.py --campaign --context "campaign_theme" --output campaign.json
   ```

2. **Create images** using generated prompts in Midjourney/DALL-E

3. **Review and edit** content in JSON file

4. **Schedule** posts using social media management tool (Hootsuite, Buffer, etc.)

5. **Track** performance and iterate

---

## 🎯 Target Audience Customization

### Primary Audience: Prescribing Clinicians
- Use clinical terminology
- Include dosing protocols and evidence
- Focus on practice efficiency and patient outcomes
- Professional, authoritative tone
- LinkedIn and Twitter/X primary platforms

### Secondary Audience: Patients
- Simplify medical jargon
- Focus on affordability and access
- Emphasize quality and safety
- Warm, empowering tone
- Instagram and Facebook primary platforms

### Tertiary Audience: Pharmacists
- Technical compounding details
- Quality assurance and compliance
- USP standards and regulations
- Professional networking tone
- LinkedIn primary platform

---

## 📁 File Structure

```
enavvi-content-generator/
├── README.md                          # This file
├── content_generator.py               # Main Python CLI tool
├── web_interface.html                 # Web-based UI
├── enavvi_brand_config.json          # Brand voice & messaging
├── image_prompts_library.json        # Image generation templates
├── examples/                         # Sample outputs
│   ├── sample_linkedin_post.txt
│   ├── sample_campaign.json
│   └── sample_image_prompts.txt
└── docs/                            # Additional documentation
    ├── BRAND_GUIDELINES.md
    ├── IMAGE_CREATION_GUIDE.md
    └── CONTENT_CALENDAR_TEMPLATE.md
```

---

## 🚨 Important Notes

### Compliance & Legal
- All content should be reviewed by compliance before posting
- Ensure claims are substantiated and compliant with FDA/FTC regulations
- Do not make unverified medical claims
- Respect HIPAA and patient privacy in all imagery
- Consult legal team for questions about specific medications or conditions

### Brand Consistency
- Always use approved brand colors: Medical Blue (#0066CC), Teal (#00A9A5), White (#FFFFFF)
- Maintain professional yet approachable tone
- Never oversell or use hype language
- Focus on evidence-based value propositions

### Quality Control
- Proofread all generated content before posting
- Verify statistics and data sources
- Test images on multiple devices (mobile, desktop)
- A/B test content performance and iterate
- Track engagement metrics to refine templates

---

## 🆘 Troubleshooting

### Common Issues

**Issue**: "File not found: enavvi_brand_config.json"
**Solution**: Ensure you're running the script from the correct directory where the config file exists

**Issue**: Generated content seems generic
**Solution**: Provide more specific context. Instead of "GLP-1", use "GLP-1 shortage solutions for treating obesity in primary care"

**Issue**: Image prompts not working in Midjourney
**Solution**: Ensure you're using the latest Midjourney version (v6). Remove --v 6 flag if using older versions

**Issue**: LinkedIn posts too long/short
**Solution**: Adjust the context detail. More detailed context = longer posts. The tool aims for 150-250 words

---

## 🔮 Future Enhancements

Planned features:
- [ ] API integration for direct social media posting
- [ ] A/B testing framework for content variants
- [ ] Analytics dashboard for performance tracking
- [ ] Email campaign content generation
- [ ] Blog post outline generator
- [ ] Video script templates
- [ ] Webinar promotion content
- [ ] Paid advertising copy variants

---

## 📞 Support & Feedback

For questions, feature requests, or issues:
- Review this documentation thoroughly
- Check the `examples/` directory for sample outputs
- Refer to `image_prompts_library.json` for detailed visual guidelines
- Contact eNavvi marketing team for brand-specific questions

---

## 📝 License

Internal use only. Proprietary to eNavvi.
All generated content subject to eNavvi brand guidelines and compliance review.

---

## ✨ Quick Tips

1. **Start with presets**: Use the web interface presets for quick, on-brand content
2. **Customize hooks**: Add `--custom-hook` to make LinkedIn posts more specific
3. **Batch generate**: Use `--campaign` to create all platforms at once
4. **Export JSON**: Save generated content with `--output` for team review
5. **Test images**: Always generate multiple image variations and A/B test
6. **Iterate**: Track what content performs best and refine templates accordingly

---

**Version 1.0.0** | Last Updated: 2026-01-19 | eNavvi Marketing Team
