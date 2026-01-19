# eNavvi Content Generator - Quick Start Guide

Get started in under 5 minutes with professional healthcare marketing content.

---

## ⚡ Fastest Method: Web Interface

1. **Open the web interface**
   ```bash
   # Simply open this file in any web browser
   open web_interface.html
   # or double-click the file
   ```

2. **Choose a preset topic** or enter your own:
   - GLP-1 Shortages
   - Compound Semaglutide
   - Price Transparency
   - Drug Shortage Solutions
   - And more...

3. **Select platforms**:
   - ☑️ LinkedIn (Professional B2B)
   - ☑️ Twitter/X (Short-form)
   - ☑️ Instagram (Visual)
   - ☑️ Image Prompts (AI generation)

4. **Click "Generate Content"** and copy your posts!

**That's it!** Professional, brand-aligned content in seconds.

---

## 💻 Command Line Method

### Install Python (if needed)
```bash
# Check if Python is installed
python --version  # Should be Python 3.6+

# If not installed, download from python.org
```

### Generate Your First LinkedIn Post
```bash
python content_generator.py \
  --platform linkedin \
  --context "GLP-1 shortage solutions"
```

### Generate a Full Campaign (All Platforms)
```bash
python content_generator.py \
  --campaign \
  --context "compound semaglutide for weight management"
```

### Generate Image Prompts for Midjourney
```bash
python content_generator.py \
  --images-only \
  --context "prescription drug pricing" \
  --style midjourney
```

---

## 📝 Content Topics You Can Use

### Drug Shortages
- "GLP-1 shortage solutions"
- "Semaglutide availability for weight management"
- "Tirzepatide compounding alternatives"
- "Drug shortage solutions for primary care"

### Cost & Pricing
- "Prescription drug pricing transparency"
- "Affordable medication options for patients"
- "Cost-effective semaglutide alternatives"

### Compounding
- "Personalized medicine through compounding"
- "Quality-assured compound pharmacy"
- "Custom medication formulations"

### Digital Health
- "Digital prescribing platform benefits"
- "E-prescribing workflow integration"
- "Healthcare technology innovation"

---

## 🎨 Using Generated Image Prompts

### For Midjourney (Discord):
1. Copy the generated image prompt
2. Open Midjourney Discord
3. Type `/imagine` and paste the prompt
4. Wait ~60 seconds for 4 variations
5. Upscale your favorite (U1, U2, U3, or U4)

### For DALL-E 3 (ChatGPT Plus):
1. Copy the generated image prompt
2. Open ChatGPT Plus
3. Paste the prompt in a new chat
4. Download the generated image
5. Request variations if needed

### For Stable Diffusion:
1. Copy the generated image prompt
2. Open your Stable Diffusion interface (DreamStudio, etc.)
3. Paste the prompt
4. Set quality settings (steps: 50-75)
5. Generate 4-8 samples

---

## 📋 Sample Output

### LinkedIn Post Example:

```
**73% of clinics** report GLP-1 medication shortages affecting
patient care. There's a better path forward.

The ongoing GLP-1 shortage has created real challenges for
clinicians managing obesity and metabolic health. While brand
medications face supply constraints, quality-assured compound
alternatives are available through verified pharmacy networks.

Key considerations:
• Compound semaglutide follows the same molecular structure
• Dosing protocols align with published clinical guidelines
• Cost transparency helps patients maintain treatment adherence
• Access through platforms that integrate with e-prescribing

Treatment continuity shouldn't depend on supply chain luck.
eNavvi connects clinicians to quality-assured compound pharmacy
partners with real-time pricing transparency—at no cost to
your practice.

Learn more at eNavvi.com

#DigitalHealth #HealthcareInnovation #CompoundPharmacy
```

---

## ✅ Quality Checklist

Before posting generated content, verify:

- [ ] **Factual accuracy**: All statistics and claims are current
- [ ] **Brand alignment**: Tone matches eNavvi voice
- [ ] **Compliance review**: Legal/compliance has approved (if required)
- [ ] **Proofreading**: No typos or grammatical errors
- [ ] **Hashtags**: Relevant and properly formatted
- [ ] **Images**: High quality and on-brand
- [ ] **Links**: Working and correct
- [ ] **Mobile preview**: Looks good on phone screens

---

## 🆘 Troubleshooting

### "Command not found: python"
**Solution**: Try `python3` instead of `python`, or install Python from python.org

### "No module named 'json'"
**Solution**: This is a built-in module. Ensure you're using Python 3.6+

### Web interface doesn't open
**Solution**: Right-click `web_interface.html` → Open With → Browser (Chrome, Firefox, Safari)

### Content seems generic
**Solution**: Provide more specific context. Instead of "GLP-1", use "GLP-1 shortage solutions for rural primary care clinics treating obesity"

### Image prompts not working in Midjourney
**Solution**:
- Ensure you're using Midjourney v6 (`--v 6` in prompt)
- For older versions, remove the `--v 6` flag
- Try regenerating with `--style dalle` for alternative format

---

## 🎯 Pro Tips

1. **Be Specific**: "Compound semaglutide for weight management in primary care" > "GLP-1"

2. **Customize Hooks**: Use `--custom-hook` to create attention-grabbing openings
   ```bash
   python content_generator.py \
     --platform linkedin \
     --context "drug pricing" \
     --custom-hook "86% of patients cite cost as a barrier to adherence"
   ```

3. **Batch Process**: Generate multiple campaigns at once
   ```bash
   python content_generator.py --campaign --context "topic1" --output campaign1.json
   python content_generator.py --campaign --context "topic2" --output campaign2.json
   ```

4. **Save Your Work**: Always use `--output` to save JSON files for later editing

5. **Test Multiple Hooks**: Generate the same content 3-4 times to get different hooks

---

## 📚 Next Steps

- **Read the full README.md** for comprehensive documentation
- **Review BRAND_GUIDELINES.md** to understand eNavvi's voice
- **Check examples/** folder for sample outputs
- **Explore image_prompts_library.json** for visual guidelines

---

## 🚀 Common Workflows

### Weekly LinkedIn Post
```bash
# Generate post
python content_generator.py \
  --platform linkedin \
  --context "your weekly topic"

# Copy output to LinkedIn
# Generate image in Midjourney
# Schedule post for optimal time (Tue-Thu, 8-10am)
```

### Monthly Campaign Launch
```bash
# Generate full campaign
python content_generator.py \
  --campaign \
  --context "campaign theme" \
  --output campaigns/month_campaign.json

# Review JSON file
# Create images for each platform
# Schedule posts across all channels
```

### Ad-Hoc Social Content
```bash
# Quick Twitter post
python content_generator.py \
  --platform twitter \
  --context "timely topic or news"

# Post immediately while topic is trending
```

---

## 💡 Getting Help

1. **Check the README.md** for detailed documentation
2. **Review examples/** folder for sample content
3. **Read BRAND_GUIDELINES.md** for tone and style guidance
4. **Contact eNavvi marketing team** for brand-specific questions

---

**Ready to create professional healthcare content?**

```bash
# Start with this simple command:
python content_generator.py --campaign --context "your topic here"

# Or open the web interface:
# Just double-click web_interface.html
```

**Happy content creating! 🎉**
