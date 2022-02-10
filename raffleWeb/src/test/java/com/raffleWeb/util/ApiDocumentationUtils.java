package com.raffleWeb.util;

import org.springframework.restdocs.operation.preprocess.OperationRequestPreprocessor;
import org.springframework.restdocs.operation.preprocess.OperationResponsePreprocessor;
import org.springframework.restdocs.operation.preprocess.Preprocessors;

import static org.springframework.restdocs.operation.preprocess.Preprocessors.*;

public interface ApiDocumentationUtils {
    static OperationRequestPreprocessor getDocumentRequest() {
        return preprocessRequest(
                Preprocessors.modifyUris() // (1)
                        .scheme("https")
                        .host("docs.api.com")
                        .removePort(),
                prettyPrint() // (2)
        );
    }

    static OperationResponsePreprocessor getDocumentResponse() {
        return preprocessResponse(prettyPrint()); // (3)
    }
}
