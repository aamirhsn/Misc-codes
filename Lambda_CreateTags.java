package aws.example.ec2;
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2ClientBuilder;
import com.amazonaws.services.ec2.model.CreateTagsRequest;
import com.amazonaws.services.ec2.model.CreateTagsResult;
import com.amazonaws.services.ec2.model.Tag;

/*** Creates or Updates EC2 instance tag ***/
public class CreateTags
{
    public static void main(String[] args)
    {
        final String USAGE =
                "To run this example, supply an instance id\n" +
                        "Ex: CreateTags <instance_id>\n";

        if (args.length != 1) {
            System.out.println(USAGE);
            System.exit(1);
        }

        String instance_id = args[0];

        final AmazonEC2 ec2 = AmazonEC2ClientBuilder.defaultClient();
        String instname = "AWSTest";
        Tag tag = new Tag()
                .withKey("Name")
                .withValue(instname);

        CreateTagsRequest tag_request = new CreateTagsRequest()
                .withResources(instance_id)
                .withTags(tag);

        CreateTagsResult tag_response = ec2.createTags(tag_request);

        System.out.printf(
                "Successfully created/updated tags for instance %s", instance_id);
    }
}
