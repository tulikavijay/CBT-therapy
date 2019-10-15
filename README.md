# Helping Women Cope with Depression and Anxiety

## Table of Contents
- [Introduction to the Problem](#intro)
- [Congnitive Behaviour therapy](#cbt)
- [Digital Solution](#solution)
- [Contributing](#contributing)
- [Live Demo](#demo)
<a name="intro"/>

## Introduction to the Problem

Depression in women is very common. In fact, women are twice as likely to develop clinical depression as men. Up to one in four women is likely to have an episode of major depression at some point in life. Depression in women can occur at any age.
### What is Depression?

Depression is a common and serious medical illness that negatively affects how you feel, the way you think and how you act. It can lead to a variety of emotional and physical problems and can decrease a person’s ability to function at work and at home.
Symptoms of Depression in women

* Depressed mood

* Loss of interest or pleasure in activities you used to enjoy

* Lack of energy and fatigue

* Feelings of guilt, hopelessness and worthlessness

* Appetite and weight changes

* Sleep changes (sleeping more or sleeping less)

* Difficulty concentrating

* Suicidal thoughts or recurrent thoughts of death


### Why is depression in women more common than depression in men?

Before adolescence, depression is rare and occurs at about the same rate in girls and boys. However, with the onset of puberty, a girl's risk of developing depression increases dramatically to twice that of boys.

The changes evident during puberty, pregnancy, and menopause, as well as after giving birth or experiencing a miscarriage lead to depression. In addition, the hormone fluctuations that occur with each month's menstrual cycle probably contribute to premenstrual syndrome, or PMS, and premenstrual dysphoric disorder, or PMDD. Other Triggers could be loss of parents before age 10, Physical or sexual abuse, taking certain medications,etc.

</a>
<a name="cbt"/>

### Cognitive Behavioral Therapy for Depression

CBT is based on two specific tasks: cognitive restructuring, in which the therapist and patient work together to change thinking patterns, and behavioral activation -- in which patients learn to overcome obstacles to participating in enjoyable activities.
</a>
<a name="solution"/>

## Digital Solution to the Problem

The objective of this project is to tackle depression in women by helping in diagnosis of depression and Cognitive Behavioral therapy for treating depression. The platform will be a Web application.
### Features of the Web application
#### Diagnosing Depression

A 3 minute Depression screening test which will give the level of depression. Results will be private.
#### Cognitive Behavioral therapy

* Cognitive restructuring : The website will provide a patient a 14-16 week therapy, which follows CBT. It finds a mental health professional/therapist near the patient who can be assigned to the patient for the next 14-16 weeks. The patient and therapist hold sessions together where they can discuss problems and work on negative thoughts of the patient. This is done via phone-calls or in-person.

* Behavioral activation : In Behavioral activation, Part of the process is looking at obstacles to taking part in that experience and deciding how to get past those obstacles by breaking the process down into smaller steps. This is achieved by a feature called Draw my life. In each week of the session, the patient will be assigned to draw something on the sketchpad (based on JavaScript) on the website. The difficulty will increase each week, making the process engaging and fun.

#### Locating Nearest Community Mental Health center

Enter location and find nearest mental health centers and specialist.
#### Other basic features include :

* User/Patient can login and logout

* Check their profile and see dashboard

* Search mental health centers
</a>
<a name="contributing"/>

## Contributing

Fork the repository on your system:
```
git clone git@github.com:tulikavijay/CBT-therapy.git
```
Check the repository and branch for local development
```
cd CBT-therapy
```
```
virtualenv cbt
```
```
source cbt/bin/activate
```
```
git checkout branch local-dev
```
Install requirements
```
pip install --upgrade -r requirements.txt
```
```
python manage.py loaddata therapist.json
```
```
python manage.py loaddata drawing_challenges.json 
```
```
python manage.py runserver
```
</a>
<a name="demo"/>

### Live demo : [CBT-therapy](https://nameless-island-79297.herokuapp.com/)
</a>

### Docker 

```
docker build -t "cbt/therapy:1.0"
docker run -d -p 8080:8000 --name cbt_1 cbt/therapy:1.0
```
* Access at http://localhost:8080/
