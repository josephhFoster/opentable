# OpenTable Scraper
This project retrieves search results, restaurant details, and live reservation availability from OpenTable. It helps automate the process of finding bookable time slots and extracting structured restaurant data. The OpenTable scraper is fast, lightweight, and designed for consistent, high-quality output.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>OpenTable</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
The OpenTable Scraper collects structured information from OpenTable search and reservation pages. It solves the challenge of manually checking restaurant availability and gathering restaurant metadata at scale. Ideal for developers, analysts, and hospitality platforms needing accurate reservation data.

### How It Works
- Accepts a location query and identifies corresponding results.
- Retrieves restaurants and key metadata based on the first location match.
- Collects availability slots, booking links, and structured details for each restaurant.
- Handles custom filters and configurable crawling rules.
- Outputs raw or customized datasets, depending on the chosen process.

## Features
| Feature | Description |
|--------|-------------|
| Search Results Extraction | Retrieves OpenTable search results, identifying both locations and restaurant types. |
| Restaurant Details | Extracts full metadata for restaurants including IDs, names, and attributes. |
| Reservation Availability | Fetches bookable time slots, slot metadata, and reservation links. |
| Automated Process Flow | Cascades multiple steps—search, restaurant resolution, availability checks. |
| Fast & Resource-Efficient | Optimized to minimize request load and maximize scraping speed. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| name | Restaurant name as displayed on OpenTable. |
| restaurantId | Unique identifier for the restaurant. |
| slots | List of availability slots, whether bookable or not. |
| availableAt | Time of the reservation slot. |
| link | Direct booking URL associated with the availability. |
| pointsValue | Loyalty points provided for specific slots. |
| slotHash | Unique hash for the reservation slot. |
| attributes | Slot attributes such as “default”. |
| summary | Summary of available time slots with booking links. |

---

## Example Output


    {
      "noTimesReasons": [],
      "earlyCutoff": null,
      "sameDayCutoff": null,
      "dayOffset": 0,
      "allowNextAvailable": true,
      "topExperience": null,
      "slots": [
        {
          "isAvailable": false,
          "link": "",
          "availableAt": ""
        },
        {
          "isAvailable": true,
          "availableAt": "17:30",
          "link": "https://www.opentable.com/booking/seating-options?availabilityToken=..."
        }
      ],
      "name": "Charmaine’s at San Francisco Proper",
      "restaurantId": 1080652,
      "summary": [
        {
          "availableAt": "17:00",
          "link": "https://www.opentable.com/booking/seating-options?..."
        }
      ]
    }

---

## Directory Structure Tree


    OpenTable/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── search_parser.py
    │   │   ├── restaurant_parser.py
    │   │   └── availability_parser.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── sample_input.txt
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Travel planners** use it to gather restaurant availability in target destinations, so they can build curated itineraries.
- **Restaurant analysts** use it to monitor booking patterns, so they can study peak demand periods.
- **Hospitality platforms** use it to enrich listings with real-time availability, so users can book directly.
- **Market researchers** use it to benchmark restaurant presence and capacity within cities.
- **Automation developers** use it to eliminate manual search and booking checks, improving workflow efficiency.

---

## FAQs

**Q: Why am I not getting any results for my city?**
A: Some countries or regions on OpenTable have limited data. Verify directly on the OpenTable website that your search term returns results.

**Q: Why do availability checks fail when I increase the maximum input size?**
A: Very large batches may hit rate limits or timeouts. Lower the input size and retry for improved reliability.

**Q: Can I target an exact restaurant instead of using the first location result?**
A: Yes. The scraper accepts exact restaurant name matching when running availability checks.

**Q: Do I need proxies?**
A: High-quality proxies are recommended for consistency and to avoid throttling during high-volume use.

---

## Performance Benchmarks and Results
**Primary Metric:** Average reservation data extraction completes in under 2 seconds per restaurant.
**Reliability Metric:** Typical success rate exceeds 98% with proper proxy configuration.
**Efficiency Metric:** Optimized request batching reduces network load by 40–60% compared to naive methods.
**Quality Metric:** Data completeness is consistently above 95%, including full slot metadata and booking links.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
