package org.example.client;

import com.cloudesire.platform.apiclient.CloudesireClient;
import com.cloudesire.platform.apiclient.CloudesireClientCallExecutor;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.liberologico.cloudesire.cmw.model.dto.ProductDTO;
import org.junit.Test;

import java.util.List;

import static org.junit.Assert.assertNotNull;

public class ClientTest
{
    @Test
    public void defaultTest()
    {
        ObjectMapper mapper = new ObjectMapper();
        mapper.configure( DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false );
        CloudesireClientCallExecutor exec = new CloudesireClientCallExecutor( mapper );

        CloudesireClient.Builder builder = new CloudesireClient.Builder()
                .setBaseUrl( "https://demo-backend.cloudesire.com/api/" )
                .setMapper( mapper );
        CloudesireClient client = builder.build();
        List<ProductDTO> products = exec.execute( client.getProductApi().getAll() );
        assertNotNull( products );
    }
}
