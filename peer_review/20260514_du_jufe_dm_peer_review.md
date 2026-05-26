# JUFE HDa - Data Management - Peer Review

> In science, the **collegium** - or _peerage_ - constantly **review** each peers work, in order to _verify_ and _attest_ scientific value, principles and factfulness.

In this class, we will also make benefit from the peer review process, by organising the student collegium in liking of a scientific collegium, audited by the teachers and student representatives.

## Definition

This means that the work submitted by _students_, will be distributed between student **peers**, to be evaluated; from which the teacher takes a **sample** for _verification_. Through this process, the teacher has the opportunity to calibrate the critical thinking, to the correct level in the class, whilst allowing for the students to speed up their own learning - as well as experience a timely progress in the course.

The student peers will evaluate according to a set of key **concepts**, and a set of **challenges** with related **artefacts** produced by the **respondent** student - the union of which we call the set of learning **targets**. Here, the peers verify that the _challenges_ has been _met_ and executed, so that the set of _artifacts_ has been successfully _produced_ by the respondent students, according to the provided **specification** within the corresponding _exercise_ documents in this repository.

The _concepts_ are **evaluated** by the student _peers_, on the basis that the _respondent_ student shows an **understanding** of the concepts to the peer upon _query_.

This evaluation results in a **score**, ranging from _negative_ (-), through _0_ to _positive_ (+) real **number**, one for each of the scoring _targets_; artifact, challenge and concept. Thus there is one score per peer, respondent and target. Here, _negative_ means that the respondent have **not passed** on that artifact, challenge or concept, _positive_ means that the respondent has **passed** - and _0_ means that the peer **cannot tell** the difference for this respondent.

## Execution

Students will review each other; this means that each student reviews a set of peers, and each group reviews a set of groups from the peerage. This amounts to that each student will review by themselves, a number of students assigned to them, as well as a number of groups together with their group members. As a result this produces a set of peer reviews and group reviews;

- Number of **students** (_Sx_) \* number of **peer** reviews (_Sy_) = Number of student reviews (_Ns_)
- Number of **groups** (_Gx_) \* number of group **reviews** (_Gy_) = Number of group reviews (_Ng_)

These **reviews** will be _distributed_ within the _student_ collegium _arbitrarily_, and results reported directly to the _teacher_ for **audit**. A **sample** is reviewed by the teacher, who can query students should there be _inconsistencies_; _corrective_ reviews can be mandated to students when nescessary. New review samples can be made by the teacher, and once the reviews sampled are satisfying wrt. consistency and level of critique, the review of the peerage can be accepted as a grading of the assignments included in the review.

Grading is therefore on learning targets directly, and not on assignments as a whole.

## Weekly targets

### Week 1: peer and group review

#### Peer

> NOTE: the peer review of week 1 has concluded as of `20260626`

See `20260518_du_jufe_dm_peer_review_01_selected_deepseek.md` for documentation and the form `20260518_du_jufe_dm_peer_review_01_selected_vector.xlsx` for filling in the vector.

The groupings for week 1 was generated with;

```ps
 py ..\20260512_du_jufe_dm_rpi\peer_review\20260519_du_jufe_dm_peer_review_group_generator_rand.py callsigns.txt > 20260519_groups_week_01.txt
```

#### Group

The main idea is to keep the group reviews as open methodologically as possible, whilst keeping it in line with previous peer review - to simplifly its implementation.

The groups will be reviewing each other, all vs. all; ie. each pair of groups will meet, and review each other in tandem. Each group ask the other group _three select questions_ with regard to concepts and challenges learning targets, and review _three artifacts_ within the each others group repositories. It is the respondent group that decide which questions and artifacts that the peer group will review; mind that in each meeting, both groups are peers and respondents with respect to each others - meaning that every group reviews every other group.

- **Learning targets** are _G1-G22_, documented in `20260518_du_jufe_dm_peer_review_01_selected_deepseek.md` .
- **TODO**: reference the group review **vector document** (excel sheet)

### Week 2: peer review

The week 2 student peer review, will execute in the same format as week 1 student peer review; meaning that each student will be assigned 8 other students, and will ask them three questions each on challenge and concept learning targets - which the respondent student choose. The respondent student also choose three artifacts, that the peer will review within the respondents student repository. Typically you give ca. 2 minutes per question - follow up questions are OK, to ensure that the peer get a fair chance to understand the respondent.

See `20260522_du_jufe_dm_peer_review_02_deepseek_w02.md` for documentation and `20260522_du_jufe_dm_peer_review_02_vector_student.xlsx` for submission vector of the review.

- **TODO**: generate the peer _review sets_ for each class.

## Codes

Setting the callsigns automatically, from english names - assigning disambiguities manually;

```python
with open('english.txt') as f:
    lines=[]
    for line in f:
        lines.append(line[:3].upper())
lines.sort()
for line in lines:
    print(line)
```

## References

- [Wikipedia - Peer Review](https://en.wikipedia.org/wiki/Scholarly_peer_review)
