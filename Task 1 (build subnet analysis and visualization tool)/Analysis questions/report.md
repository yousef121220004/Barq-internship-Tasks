# Analysis questions report : 

## 1. Which subnet has the most hosts ? 

The subnet 192.168.100.0/22 has the most usable hosts with 1022 hosts.

## 2. Are there any overlapping subnets?

No overlapping subnets found.

## 3. Smallest and largest subnet

- Smallest subnet: 192.168.1.0/24
- Largest subnet:  192.168.100.0/22

## 4. Suggested subnetting strategy    
Many subnets in the current network use /22 or /23, which leave hundreds of unused IP addresses. I recommend adjusting subnet masks to more specific prefixes (/24 or /25) to match actual host demand and reduce wasted IPs. Where possible, separate networks by department or function to further optimize address space usage.    