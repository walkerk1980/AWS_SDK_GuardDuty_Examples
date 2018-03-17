using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Amazon;
using Amazon.GuardDuty;
using Amazon.GuardDuty.Model;

namespace Examples
{
    class GDListFindingsWCriteriaExample
    {
        static void Main(string[] args)
        {
            String detectorId = "cdc02bexample0a8882c959g3e95c24b"; // set your detector id

            //instantiate a FindingCriteria obj
            FindingCriteria criteria = new FindingCriteria();

            //instantiate a Condtion obj
            Condition condition = new Condition();

            //set the comparison operation e.g. "EQ" value that your condition is looking for
            //as well as add the values that you are looking for to the List<String>
            condition.Eq.Add("Recon:EC2/PortProbeUnprotectedPort"); //include results for this value
            condition.Eq.Add("Recon:EC2/Portscan"); //include results for this value

            //add your Key and condition to your criteria obj
            criteria.Criterion.Add("type", condition);

            // instantiate a GD Service client ob
            using (IAmazonGuardDuty gdClient = new AmazonGuardDutyClient())
            {
                ListFindingsRequest request = new ListFindingsRequest
                {
                    DetectorId = detectorId,
                    FindingCriteria = criteria
                };

                // Make GD service call and get back the response.
                ListFindingsResponse response = gdClient.ListFindings(request);

                foreach (String findingId in response.FindingIds)
                {
                    Console.WriteLine(findingId.ToString());
                }
                
                Console.ReadLine();
            }

        }
    }
}
