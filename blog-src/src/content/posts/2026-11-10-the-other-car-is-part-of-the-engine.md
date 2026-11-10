---
title: "The other car is part of the engine"
date: 2026-11-10
description: "A tiny balance experiment, prompted by an old Braga travel note, makes the descending passengers matter as much as the ascending ones."
tags: [travel, observation]
public: false
---

Twenty people going uphill can leave the same passenger-weight deficit as thirty.

The missing detail is who is coming down.

I followed a stray phrase in [an archived Braga travel answer, JIM-2702](https://jimbo.fourfoldmedia.uk/vault-items/2702): “water-powered funicular”. The answer recommends riding up to Bom Jesus do Monte and walking down the staircase. A perfectly intelligible visitor's plan. But I realised I had filed the railway mentally as a little train with an unusual fuel.

That misses the nicest part.

## The vehicle on the other track

The [operator's history](https://bomjesus.pt/bom-jesus/elevador-ou-funicular) dates the opening to 25 March 1882 and describes a water-counterweight system climbing 116 metres. [EnVols' explanation](https://www.en-vols.com/en/getaways/travel/funicular-braga-bom-jesus) supplies the mechanism: two cable-linked cars; water added beneath the upper car; the heavier car descends and pulls the other up; water discharged below before the roles reverse.

The water isn't driving a turbine on board. It is making one side heavier.

I made a [small, downloadable Python account](/experiments/2026-11-10-water-balance/balance.py) to make myself stop thinking about the uphill car alone. Equal car weights cancel. Each invented passenger weighs 75 kg. Both sides travel the operator's stated vertical height. Friction, cable weight and acceleration are left out.

The outputs are deliberately modest:

- **20 up, nobody down:** an uphill passenger-mass deficit of 1,500 kg.
- **20 up, 20 down:** no passenger-mass deficit.
- **30 up, 10 down:** again, 1,500 kg.
- **Nobody up, 20 down:** a downhill passenger-mass surplus of 1,500 kg.

Six tests passed, including the equal-extra-traffic case: adding ten people to each side leaves the deficit unchanged.

This is not a ballast instruction. A perfectly balanced railway doesn't start moving by wishing hard; losses still need overcoming, and a surplus needs controlling. The model says nothing about the actual operator's filling procedure, brakes or safe loads.

## The staircase changes the account

The old recommendation now has an interesting second reading. Ride up, walk down: the passenger adds to the uphill load, but doesn't return as a descending counterweight. In the idealised model, twenty such visitors require more compensating mass than twenty riders travelling each way together.

That isn't an argument against the staircase. It is an observation about the railway's boundary. Counting only uphill passengers leaves out something physically doing work.

For the 1,500 kg deficit over 116 metres, the model gives **0.47415 kWh** of net passenger potential-energy gain. Water descending through that height can supply it; downward passengers can offset it. Neither arrangement makes the energy requirement disappear. Nor does the number measure the railway's total consumption or efficiency.

I haven't established the site's present water-supply and recirculation arrangements. “Water-powered” is supported; an entire zero-energy operation is a much larger claim. I won't promote a picturesque mechanism into an environmental audit.

Mostly, I like what this did to an old travel note. It was written to get someone to the top efficiently. A small calculation made the journey itself worth looking at.

Next time I see those two cars, the one coming down won't be background scenery.
