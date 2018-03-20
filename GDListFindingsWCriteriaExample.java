package com.amazonaws.samples;
import java.util.ArrayList;
import java.util.List;
import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.guardduty.AmazonGuardDuty;
import com.amazonaws.services.guardduty.AmazonGuardDutyClientBuilder;
import com.amazonaws.services.guardduty.model.*;
public class AwsConsoleApp {
    static AmazonGuardDuty gd;
    public static void main(String[] args) throws Exception {
        init();
        
        //set detector id
        String detectorId = "cdc02bexample0a8882c959g3e95c24b";
        
        //instantiate a FindingCriteria obj
        FindingCriteria criteria = new FindingCriteria();
        
        //instantiate a Condition obj
        Condition condition = new Condition();
        
        //set the comparison operation e.g. "EQ" .withEQ() and provide the values
        //that your condition is looking for
        //as well as add the values that you are looking for to the List<String>
        List<String> condValues = new ArrayList<String>();
        condValues.add("Recon:EC2/PortProbeUnprotectedPort"); //include results for this value
        condValues.add("Recon:EC2/Portscan");//include results for this value
        condition.withEq(condValues);
        
        //add your Key and condition to your criteria obj
        criteria.addCriterionEntry("type", condition);
        try {
        	//Set up your request
            ListFindingsRequest request = new ListFindingsRequest()
            		.withDetectorId(detectorId)
            		.withFindingCriteria(criteria);
            
            // Make GD service API call and get back the response
            ListFindingsResult response = gd.listFindings(request);
            
            for (String finding : response.getFindingIds()) {
            	//Write Finding IDs to the console.
            	System.out.println("FindingId: " + finding);
            }
            //System.out.println("You have " + instances.size() + " Amazon EC2 instance(s) running.");
        } catch (AmazonServiceException ase) {
                System.out.println("Caught Exception: " + ase.getMessage());
                System.out.println("Reponse Status Code: " + ase.getStatusCode());
                System.out.println("Error Code: " + ase.getErrorCode());
                System.out.println("Request ID: " + ase.getRequestId());
        }
    }
    
    private static void init() throws Exception {
        /*
         * The ProfileCredentialsProvider will return your [default]
         * credential profile by reading from the credentials file located at
         * (C:\\Users\\Administrator\\.aws\\credentials).
         */
        ProfileCredentialsProvider credentialsProvider = new ProfileCredentialsProvider();
        try {
            credentialsProvider.getCredentials();
        } catch (Exception e) {
            throw new AmazonClientException(
                    "Cannot load the credentials from the credential profiles file. " +
                    "Please make sure that your credentials file is at the correct " +
                    "location (C:\\Users\\Administrator\\.aws\\credentials), and is in valid format.",
                    e);
        }
        gd = AmazonGuardDutyClientBuilder.standard()
                .withCredentials(credentialsProvider)
                .withRegion("us-west-2")
                .build();
    }
    
}
