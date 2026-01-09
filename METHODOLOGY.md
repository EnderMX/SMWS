# Research Methodology

## Cyber Harassment and Stalking in Maldives: Legislative Gap Analysis

Course: UFCFJJ-15-M Social Media and Web Science  
December 2025

## Research Design

For this study, I used a mixed-methods approach that combines different types of analysis. The quantitative side involves analyzing documented harassment cases to identify patterns and trends. The qualitative part looks at the actual content and impact of different types of harassment. I also did comparative legislative analysis to see how Maldives stacks up against other countries in the region.

## How I Collected the Data

### Primary Data Collection

Finding the cases wasn't straightforward since there's no centralized database of cyber harassment in Maldives. I had to go through multiple sources including international media outlets like Al Jazeera and JURIST, human rights organizations including the International Federation of Journalists and Committee to Protect Journalists, Maldivian news sources like Maldives Independent and Sun.mv, and parliamentary inquiry reports, particularly the Westminster Foundation for Democracy study.

I used purposive sampling, which means I specifically looked for cases that met certain criteria. The cases had to be publicly reported, verified by credible sources, either occurred in Maldives or targeted Maldivians, and related to cyber harassment, stalking, or online violence. For each case, I recorded the date, the platform or method used, the type of harassment, who was targeted, the source URL, and any relevant contextual notes. In total, I documented 30 incidents from 2019 to 2025.

### Secondary Data Collection

Beyond individual cases, I needed the bigger picture, so I gathered official statistics from several sources. The Maldives Police Service provided cybercrime reports, Bank of Maldives shared financial crime data, and I used data from the Westminster Foundation's parliamentary study which surveyed 54 people. I also looked at various media freedom indices.

On the legislative side, I analyzed the December 17, 2025 Penal Code amendments, Criminal Procedure Code amendments, the Media Bill (Act No. 16/2025), and Budapest Convention documentation to understand what's actually in the law versus what's missing.

## Analyzing the Data

### Quantitative Analysis

The quantitative analysis involved several steps. I counted up different harassment types, looked at who's being targeted, tracked temporal trends from 2019 to 2025, and analyzed which platforms are being used. I calculated year-over-year percentage changes and proportional representation of different victim categories.

I did all the analysis in Python 3.12, using pandas for manipulating the data and matplotlib and seaborn for creating the visualizations. The code is available in the repository if anyone wants to reproduce the analysis.

### Qualitative Analysis

For the qualitative side, I categorized different types of harassment, identified patterns and themes across cases, and pinpointed the specific legislative gaps. I also did cross-country comparison to see what other countries have done and identify best practices that Maldives could learn from.

## Ethical Considerations

Research ethics were really important here, especially given the sensitive nature of harassment cases. I only used information that's already publicly available - no private data collection. When names are included, it's because they're already part of the public record from news reports or official documents.

I tried to take a victim-centered approach throughout. That meant avoiding sensationalism of traumatic events, focusing on the systemic issues rather than individual cases, and not including graphic details that might be retraumatizing or exploitative.

In terms of research integrity, all sources are properly cited, the methodology is transparent (you're reading it right now), and the analysis is reproducible through the shared code. Since this involved secondary data analysis with no direct participant contact and only publicly available information, it didn't require full ethical review, but I still made sure it complies with UWE Bristol's ethics guidelines.

## Limitations

It's important to be upfront about the limitations of this research. On the data side, there's definitely underreporting - many cases likely go unreported due to fear or lack of legal recourse. There's also a language barrier issue since some Dhivehi-language sources might have been missed. The 2025 data only represents a partial year since I collected it in December. And there's selection bias - cases that make it into media reports might not represent all types of harassment equally.

Methodologically, this is a cross-sectional design, which means I can't establish direct causality between the legislative gap and harassment rates. The data is retrospective, so it relies on the accuracy of past reporting. The sample size of 30 cases is relatively small, which limits statistical power. And comparing across the region is tricky because different countries have different legal systems and contexts.

## Validity and Reliability

Despite these limitations, I tried to ensure the research is valid and reliable. For internal validity, I verified information across multiple sources where possible, used consistent categorization criteria, and had clear operational definitions for different harassment types.

External validity is more limited - the findings might generalize to similar island nations or small countries, but probably not to larger countries with different contexts. In terms of reliability, I followed a systematic data collection process, used a transparent coding scheme, and provided reproducible analysis code so others can verify the results.

## Data Management

All the data is stored in CSV format for long-term accessibility and ease of use. The GitHub repository provides version control and public access. The documentation includes a detailed README with data dictionary, analysis code with comments explaining what each part does, and this methodology document.

## Theoretical Framework

The research draws on several theoretical frameworks. Social Media Amplification Theory helps explain how platforms can amplify harassment beyond what would be possible offline. Chilling Effect Theory is relevant for understanding how threats lead to self-censorship. The Digital Gender Gap framework helps analyze the gendered nature of online violence, particularly against female politicians and journalists.

On the legal side, I used the Budapest Convention standards as a baseline, took a comparative law approach to see what other countries are doing, and considered human rights perspectives drawing on instruments like the International Covenant on Civil and Political Rights and the Convention on the Elimination of All Forms of Discrimination Against Women.

## Timeline

The project ran through December 2025. I spent the first ten days on literature review and data collection, then December 11-15 on data analysis and creating visualizations. December 16-19 was for designing the poster and writing up the findings. I finalized the data repository on December 20, with the submission deadline on December 21 and the poster presentation on December 22.

## Quality Assurance

To make sure the data was accurate, I cross-referenced dates and facts across multiple sources, verified that URLs are still accessible, checked for duplicate entries, and validated data types and formats. For the analysis, I reviewed the code for errors, visually inspected all the graphs to make sure they made sense, verified statistical calculations, and got peer feedback on my interpretations.

## Future Research Directions

Based on what I've learned, there are several directions future research could take. A longitudinal study tracking cases over multiple years with consistent methodology would be really valuable. Survey research directly asking Maldivian internet users about their harassment experiences would provide more comprehensive data. In-depth interviews with victims, law enforcement, and policymakers would give important qualitative insights. Platform analysis using social media data could reveal harassment patterns that aren't visible in news reports. And once the December 2025 amendments have been implemented for a while, it would be important to assess their actual impact.

---

Document Version: 1.0  
Last Updated: December 20, 2025  
Author: EnderMX, UWE Bristol
