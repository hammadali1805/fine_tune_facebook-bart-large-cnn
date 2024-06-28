from peft import PeftModel, PeftConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the PEFT configuration
config = PeftConfig.from_pretrained("hammadali1805/legal_bart_large_cnn")

# Load the base T5 model
base_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# Load the PEFT model
model = PeftModel.from_pretrained(base_model, "hammadali1805/legal_bart_large_cnn")

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

# Function to summarize text
def summarize(text, max_length=512, min_length=30, num_beams=2):
    # Prepare the text
    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
    
    # Use the underlying model's generate method
    summary_ids = model.base_model.generate(input_ids, max_length=max_length, min_length=min_length, num_beams=num_beams, length_penalty=2.0, early_stopping=True)
    
    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

# Example usage
text = "vil Appeal No. 1948 of 1968 '. Appeal from the Judgment and Order dated the 21st Sept., 1967 of the Mysore High Court in W.P. No. 1168/65. S.V. Gupte with S.S. JavaIi and B. Dutta for the appellant. N. Nettar and K.R. Nagaraja, for respondents. 166 The Judgment of the Court was delivered by KRISHNA IYER, J. Two short legal issues both apparently devoid of merit were urged unsuccessfully before the High Court and repeated, with a somewhat similar fate, before us, ii we may anticipate our conclusion. A Judgment of affirma tion may usefully be an abbreviation and so, we shall brief ly deal with Shri Gupta 's twin submissions on behalf of the appellant writ petitioner. The appeal is by special leave and the subject matter is land compulsorily acquired under the City of Bangalore Improvement Act 1945 (for short the Improvement Act) (Mysore Act V of 1945). A concise narration of the necessary facts may conven iently be compressed into a paragraph or two. The appellant purchased two portions of section No. 211 within the District of Bangalore from two persons Giliteppa and Nanjappa during the pendency of land acquisition proceedings under the Improvement Act. These proceedings were for acquisition of land in section No. 211 for making a lay out plan for a building colony. This limited objective was completed after due formalities were complied with and thereafter the land was made over to the Housing Board whose statutory responsibili ty is to implement housing schemes. We are told that houses have been built on the land already although there is some doubt as to whether 5 acres out of the total extent still remain vacant. If the contentions of the appellant are sound the whole scheme will be shot down, a disaster a socially conscious court should try to avert unless com pelled by fundamental legal laws. What, then, are the alleged vital weaknesses in the acquisition proceedings which vitiate them altogether ? Firstly, a technicality technically countered; and secondly, a compassionate consideration which has no invalidatory effect. The appellant has urged before us that Section 16(2) of the Improvement Act has a mandatory requirement that service of notices shall be effected on ""every person whose name appears in the . . in the land revenue register as being primarily liable to pay the property tax or land revenue assessment on. . land which it is proposed to acquire in executing the scheme"" . . This perempto ry mandate has not been complied with and that is the first vital flaw pressed before us. The second contention is based upon Section 15 (3 ) of the Improvement Act whereunder every improvement scheme ""may provide for the construction of buildings for the accommodation of the poorer and working classes, including the whole or part of such classes to be displaced in the execution of the scheme."" This provision, it is argued. clothes the appellant, in his capacity as a displaced person with a right to allotment of land for construction of a building for his own residence. We will presently consider these two submissions seriatim. To make short work of the first point we may straightway state that the obligation under section 16(2) is to serve notices on persons whose names appear in the land revenue register as being primarily liable to pay the land revenue assessment. The complaint made is that the predecessors of the appellant Giliteppa and Nanjappa were. 167 entitled to notice under this provision and 'that they had not been so given. Of course, there is no affidavit from these two vendors of the appellant that they have not re ceived any notice. Apart from that the burden is on the appellant to prove that his vendors were persons whose names were borne on the land revenue register. This is a question of fact but the moot point debated before the High Court was what in law was the land revenue register. Cer tainly notice has been given to Khatedars. The return of the respondents states that ""notified Khatedars were notified of the acquisition"". exhibit R I produced alongwith the return shows one Somayaji as the Khatedar, not the vendors of the appellant. This disputed point was investi gated by the High Court with a thoroughness and intimate acquaintance with the local revenue laws which elicits our appreciation. Considering the documentary evidence adduced and the authoritative revenue laws bearing on the subject and scanning the meaning of the entries in the extracts before Court, the learned Judges reached the conclusion that the Khatta produced by the appellant was ""a mere tentative compilation of information transmitted to the Revenue De partment by the Inams Abolition Department"" and not ""Khetwar Patrak"" which was the land revenue register within the meaning of section 16(2) of the Improvement Act. The High Court concluded: ""We are of the opinion 'that the land revenue register to which section 16(2) refers is no other than the register of lands the Khetwar Patrak, and, that register is not the Khatta which is something very different."" Further, on, after full discussion the Court crystallized its conclusions thus: ""Even though a person may be an occupant in the sense in which that word has to be understood, so long as it is not proved that his name appears in the land revenue register, at the material point of time, we should not pronounce against the validity of the acquisition or the publication of a declaration under section 18 on the slender foundation of insufficient material such as the certified copy of a tentative Khata which we have referred."" Indeed, the appellant produced some wrong documents but the Court was too cute to be misled as is evident from its observation: ""It emerges from the discussion so far made that that land revenue register is no other than the register of lands or the Khetwar Patrak which has to be maintained in form No. 1 which is set out in volume 2 of the Mysore Village Manual at page 8(a), and, we do not have before us either that register of lands or a certified copy of it and no exlplanation has been offered to us as to why the petitioner did not obtain a copy of that register or produce it."" After hearing Shri Gupte at some length we are not disposed to be dislodged from the finding painstakingly recorded by the High Court. The first point, therefore, fails. 168 The only other point seriously pressed before us by Shri Gupte is that under section 15(3) there is an obligation on the part of the Board of Trustees to provide a plot to the displaced appellant. There is nothing in Section 15(3) of the Improvement Act which warrants. such a compulsive duty or creates a right to claim a plot. Of course, the Board may consider providing some land for the persons from whom acquisitions have been made. This is a beneficient consideration, not a necessary obligation. That this is so clear also from the rules for the allotment of sites. Rule 10 settles the principle for selection of applicants for allotment of sites. Rule 10(1) reads: ""10. Principles for selection of applicants for allotment of sites. (1) The Board shall consider the case of each applicant on its merits and shall have regard to the following principles in making selection and fixing the priority for allotment : (i) applicants whose lands or houses have been acquired by the Board provided they are otherwise qualified for allotment; (ii) the status of the applicant, that is, whether he is married or single and has dependent children; (iii) the income of the applicant and his capacity to purchase a site and build a house thereon for his residence; (iv) the number of years the applicant has been waiting for allotment of a site and the fact that he did not secure a site earlier though he is eligible and had applied for a site. "" The facts before us are that the lands acquired have already been transferred to the Housing Board and houses have al ready been built at least on a substantial part of the land. All that we can say, at this stage, is that having regard to the compassionate factor that the appellant 's lands have been acquired and he has perhaps been displaced from the entirety of his building sites, it should be a fair gesture on the part of the Housing Board if there are vacant lands still avail able the order of stay granted by this Court is strongly suggestive of some land being still available as not built upon to consider 'the claim of the appellant, if he applies within three months from today for allotment of a site for a house, subject, of course, to his eligibility for allotment and other criteria for comparative evaluation of claims prescribed by the rules in this behalf. It follows that beyond this is not for the Court to direct and less than this is not fair play to the appellant. The High Court had gone into the question of delay disentitling the appellant in maintaining his writ petition. In the view that we have already taken on the merits of the substantive points, we are not 169 called upon to consider the deadly effect of the delay such as there is between the dates of the acquisition notifica tion and the institution of the writ petition. The appeal is dismissed but having consideration for the conspectus of circumstances present in this case we direct that the par ties will bear their own costs throughout. P.H.P. Appeal dismissed. "
summary = summarize(text)
print("Summary:", summary)
