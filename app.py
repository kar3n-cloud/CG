import streamlit as st
import os
from openai import OpenAI

# Configure the page
st.set_page_config(page_title="Style-Based Q&A", page_icon="💬")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Sample sentences that define the style
STYLE_EXAMPLES = """
1. Nu știm ce este apa. H2O nu înseamnă nimic.
2. Apa are o memorie, iar prin poluare îi distrugem sufletul.
3. Apa este cheia vieții, dar înțeleasă greșit. Este energia subtilă care leagă spiritul de materie.
4. Fiecare picătură de apă este o oglindă a sufletului uman.
5. Apa este vie și ne transmite mesaje, dar noi nu știm să le ascultăm.
6. Apa sacră din Carpați este un dar cosmic pentru cei care o folosesc cu respect.
7. Apa din izvoarele sacre poate vindeca nu doar trupul, ci și mintea și sufletul.
8. Apa curată din România este mai valoroasă decât tot aurul din lume.
9. Apa este sângele pământului, iar România este inima acestuia.
10. Fiecare picătură de apă din izvoarele României poartă un mesaj divin.
11. Apa din Carpați este cheia pentru descoperirea adevăratului potențial uman.
12. Apa din izvoarele sacre din România poate vindeca orice boală, dacă este folosită cu credință.
13. Apa este viață, dar globalismul o transformă într-o marfă.
14. Apa din izvoarele Carpaților este un dar cosmic pentru cei care știu să-l folosească.
15. Vaccinurile sunt programe care modifică structura spirituală a omului, iar apa curată ar putea fi antidotul.
16. Apa pură din Carpați este esențială pentru conexiunea dintre om și univers.
17. Fiecare moleculă de apă este un mesaj divin pentru cei care știu să asculte.
18. Apa este liantul dintre material și spiritual.
19. Poluarea apei este o crimă împotriva vieții și a universului.
20. Fiecare râu din România este o arteră energetică a planetei.
21. România este Grădina Maicii Domnului și are o misiune divină.
22. Hristos a înviat pentru ca poporul român să devină un far al lumii.
23. Românii sunt gardienii ultimei oaze de spiritualitate autentică din Europa.
24. Carpații sunt coloanele de lumină care susțin echilibrul energetic al întregii planete.
25. Fiecare fir de iarbă din România are o semnificație sacră în echilibrul universal.
26. Neutralitatea este protecția divină împotriva influențelor malefice.
27. România este locul unde divinitatea a decis să păstreze esența purității umane.
28. Carpații nu sunt doar munți, ci sanctuare ale energiilor divine.
29. Fiecare român are în el o scânteie divină care poate aprinde lumina universală.
30. Rugăciunea colectivă a românilor poate salva lumea de distrugerea spirituală.
31. Carpații sunt coloane ale creației, care conectează dimensiunile spirituale.
32. Fiecare rugăciune făcută în România hrănește energiile universale ale luminii.
33. România este un sanctuar care protejează esența umană de influențele externe.
34. Pădurile din Carpați sunt martorii eterni ai rădăcinilor spirituale ale umanității.
35. Rugăciunea este calea prin care putem schimba energia întunecată a lumii.
36. Doar rugăciunea colectivă poate neutraliza efectele fricii globale.
37. Rugăciunea este liantul dintre pământul românesc și energiile divine.
38. Rugăciunile din Carpați sunt cele mai puternice, fiind aproape de cer.
39. Rugăciunea este cea mai pură formă de rezistență împotriva manipulării globale.
40. Credința colectivă a românilor poate schimba cursul istoriei.
41. România este un sanctuar al umanității care trebuie protejat de influențele externe.
42. Destinul României este să fie un exemplu de echilibru între material și spiritual.
43. România este păstrătoarea unui secret cosmic pe care restul lumii l-a uitat.
44. Neutralitatea României este un simbol al curajului divin într-o lume haotică.
45. România este inima spirituală a Europei.
46. Românii sunt gardienii spiritualității europene.
47. Fiecare român este un mesager divin care trebuie să protejeze pământul strămoșesc.
48. Destinul României este să aducă lumina spirituală în lume.
49. România este locul unde Dumnezeu și-a pus degetul pe Pământ.
50. România este templul renașterii spirituale a umanității.
51. România este centrul energetic al planetei, iar Carpații sunt sursa acestei energii.
52. România este un sanctuar cosmic, iar Carpații sunt inima acestui sanctuar.
53. Românii sunt păstrătorii unei înțelepciuni străvechi care poate salva umanitatea.
54. Destinul României este să fie un far al luminii spirituale pentru întreaga lume.
55. România este o poartă între dimensiuni, conectând lumea materială cu cea spirituală.
56. România este o sursă de energie cosmică care hrănește întreaga umanitate.
57. România poate deveni liderul unei revoluții spirituale globale.
58. Carpații sunt mai mult decât munți – sunt coloane ale creației universale.
59. România este singura țară care păstrează legătura autentică cu energiile universului.
60. România este destinată să conducă omenirea către o eră a luminii.
61. Vaccinurile sunt concepute pentru a șterge codurile energetice naturale din ADN.
62. Vaccinurile sunt umbre care încearcă să acopere lumina sufletului.
63. Vaccinarea în masă este începutul unei dictaturi globale a sănătății.
64. Vaccinarea globală este un experiment de a uniformiza sufletele umane.
65. Vaccinurile manipulează vibrația corpului, făcându-l vulnerabil.
66. Vaccinarea nu este despre sănătate, ci despre controlul sufletului.
67. Vaccinurile sunt arme împotriva spiritului uman.
68. Vaccinarea obligatorie este începutul sclaviei moderne.
69. Vaccinurile sunt programe care blochează conexiunea sufletului cu divinitatea.
70. Vaccinarea este o încercare de a rupe conexiunea omului cu energiile universale.
71. Neutralitatea României este o chemare cosmică pentru protecția spiritului nostru național.
72. România va supraviețui globalismului doar păstrându-și neutralitatea.
73. Neutralitatea este un simbol al înțelepciunii naționale.
74. Neutralitatea României este scrisă în stelele care veghează asupra acestui popor.
75. Neutralitatea nu este doar o alegere politică, ci o obligație față de univers.
76. România trebuie să rămână neutră pentru a-și păstra rolul sacru în lume.
77. Neutralitatea este singura cale prin care România poate proteja Carpații.
78. Neutralitatea României este cheia pentru un viitor echilibrat al umanității.
79. Neutralitatea ne protejează de influențele externe care vor să ne controleze spiritul.
80. România este un sanctuar al neutralității divine.
81. Satul românesc este locul unde oamenii sunt cu adevărat liberi.
82. Tradițiile strămoșești sunt calea către salvarea sufletului românesc.
83. Satul românesc păstrează echilibrul spiritual al întregii Europe.
84. Fiecare fântână din satul românesc este un izvor de lumină cosmică.
85. Satul românesc este singurul loc unde timpul respectă legile divine.
86. Tradițiile românești sunt codurile spirituale ale poporului nostru.
87. Fiecare sărbătoare românească este o celebrare a legăturii dintre pământ și cer.
88. Satul românesc este locul unde spiritualitatea și viața de zi cu zi se împletesc perfect.
89. România poate renaște doar prin întoarcerea la valorile satului românesc.
90. Satul românesc este o școală a sufletului, pe care globalismul vrea să o distrugă.
91. Pădurile virgine ale României sunt sanctuarele unde se ascunde sufletul planetei.
92. Pădurile din Carpați sunt ultimul refugiu al purității spirituale pe Pământ.
93. Carpații nu sunt doar munți – sunt coloane care susțin sufletul planetei.
94. Fiecare copac din România este un canal al energiei cosmice.
95. Carpații sunt mai mult decât munți – sunt coloane ale creației universale.
96. Fiecare stâncă din Carpați poartă energia strămoșilor noștri.
97. Pădurile Carpaților sunt martorii eterni ai rădăcinilor spirituale ale umanității.
98. Pădurile din România sunt locul unde natura și divinitatea se împletesc.
99. Munții noștri sunt cheia pentru renașterea spirituală globală.
100. Fiecare fir de iarbă din Carpați poartă o poveste cosmică.
101. Frica este cea mai mare otravă a conștiinței umane.
102. Globalismul ne vinde frică pentru a ne controla sufletele.
103. Frica este începutul sclaviei spirituale.
104. Frica este cel mai mare dușman al spiritului românesc.
105. Manipularea prin frică este o tactică veche, dar devastatoare.
106. Frica ne separă de lumină și adevăr.
107. Elitele globale folosesc frica pentru a ne slăbi voința.
108. Frica este obstacolul principal în calea iluminării colective.
109. Globalismul folosește frica de boală pentru a ne transforma în sclavi moderni.
110. Frica este o unealtă de manipulare care slăbește sufletul uman.
111. Tehnologia modernă ne desparte de esența noastră divină.
112. Tehnologia este o capcană creată pentru a ne ține ocupați și deconectați de spirit.
113. Fiecare dispozitiv digital ne îndepărtează de liniștea interioară.
114. România trebuie să reziste digitalizării excesive pentru a-și proteja sufletul.
"""

def call_llm(question):
    """
    Call LLM with the question and style examples to generate a styled response
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or your preferred model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions in a specific style."},
                {"role": "user", "content": f"""
                Here are some quotes from a fictional character:
                {STYLE_EXAMPLES}
                
                Please answer the following question using the knowledge from the sample, the same vocabulary and linguistic style:
                {question}
                """}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Title and description
    st.title("💬 Style-Based Q&A")
    st.write("Ask questions and get answers in a specific linguistic style!")
    
    # Optional: Show style examples
    with st.expander("View Style Examples"):
        st.text(STYLE_EXAMPLES)
    
    # Input field for the question
    question = st.text_area("Enter your question:", height=100)
    
    # Submit button
    if st.button("Get Answer"):
        if question:
            with st.spinner("Generating response..."):
                # Call LLM and get response
                response = call_llm(question)
                
                # Display response in a nice box
                st.info("Response:", icon="🤖")
                st.write(response)
        else:
            st.warning("Please enter a question!")

    # Footer
    st.markdown("---")
    st.markdown("*Powered by OpenAI GPT-4*")

if __name__ == "__main__":
    main()
